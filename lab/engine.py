import time
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

from config import WORDLISTS_DIR, DEMO_USERS_FILE, RESULTS_CSV, RESULTS_JSON
from lab.generator import generate_demo_users
from lab.hashing import verify_bcrypt, verify_sha256_salted, verify_sha256_unsalted
from lab.models import DemoAuditResult
from lab.policy import evaluate_password
from lab.reporter import (
    export_demo_results_csv,
    export_demo_results_json,
    print_banner,
    print_demo_audit_results,
    print_password_check,
)
from lab.risk import classify_risk
from lab.utils import load_json, load_all_wordlists_from_dir


def run_generate_mode(args) -> None:
    print_banner()
    users = generate_demo_users(args.users)
    print(f"Generated {len(users)} demo users at: {DEMO_USERS_FILE}")


def run_check_password_mode(args) -> None:
    print_banner()
    breach_words = set(word.lower() for word in load_all_wordlists_from_dir(WORDLISTS_DIR))

    password = args.password
    if not password:
        password = input("Enter password to evaluate: ").strip()

    result = evaluate_password(password, breach_words)
    risk = classify_risk(result)
    print_password_check(result, risk)


def run_breach_check_mode(args) -> None:
    print_banner()
    breach_words = set(word.lower() for word in load_all_wordlists_from_dir(WORDLISTS_DIR))

    password = args.password
    if not password:
        password = input("Enter password to check against local wordlists: ").strip()

    found = password.lower() in breach_words
    print(f"Found in local breach/common-password wordlists: {'Yes' if found else 'No'}")


def run_audit_demo_users_mode(args) -> None:
    print_banner()

    try:
        demo_users = load_json(DEMO_USERS_FILE)
    except FileNotFoundError:
        demo_users = generate_demo_users(12)

    breach_words = load_all_wordlists_from_dir(WORDLISTS_DIR)
    breach_set = set(word.lower() for word in breach_words)

    results: list[DemoAuditResult] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("Auditing demo users", total=len(demo_users))

        for user in demo_users:
            start = time.perf_counter()
            time.sleep(args.delay / 1000)

            weak_password_detected = False
            matched_from_demo_wordlist = False

            for candidate in breach_words:
                if user["hash_type"] == "sha256_unsalted":
                    if verify_sha256_unsalted(candidate, user["password_hash"]):
                        weak_password_detected = candidate.lower() in breach_set
                        matched_from_demo_wordlist = True
                        break
                elif user["hash_type"] == "sha256_salted":
                    salt = user["salt"] or ""
                    if verify_sha256_salted(candidate, salt, user["password_hash"]):
                        weak_password_detected = candidate.lower() in breach_set
                        matched_from_demo_wordlist = True
                        break
                elif user["hash_type"] == "bcrypt":
                    if verify_bcrypt(candidate, user["password_hash"]):
                        weak_password_detected = candidate.lower() in breach_set
                        matched_from_demo_wordlist = True
                        break

            elapsed = time.perf_counter() - start
            results.append(
                DemoAuditResult(
                    username=user["username"],
                    hash_type=user["hash_type"],
                    weak_password_detected=weak_password_detected,
                    matched_from_demo_wordlist=matched_from_demo_wordlist,
                    elapsed_seconds=elapsed,
                    notes="Demo local audit completed.",
                )
            )
            progress.update(task, advance=1)

    print_demo_audit_results(results)
    export_demo_results_csv(RESULTS_CSV, results)
    export_demo_results_json(RESULTS_JSON, results)
    print(f"\nExported CSV: {RESULTS_CSV}")
    print(f"Exported JSON: {RESULTS_JSON}")
