import csv
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from lab.models import DemoAuditResult, PasswordCheckResult

console = Console()


def print_banner() -> None:
    console.rule("[bold cyan]SecurePass Lab[/bold cyan]")
    console.print("[yellow]Offline password health and exposure demo toolkit[/yellow]\n")


def print_password_check(result: PasswordCheckResult, risk_level: str) -> None:
    table = Table(title="Password Health Check")
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Length", str(result.length))
    table.add_row("Uppercase", "Yes" if result.has_upper else "No")
    table.add_row("Lowercase", "Yes" if result.has_lower else "No")
    table.add_row("Digit", "Yes" if result.has_digit else "No")
    table.add_row("Symbol", "Yes" if result.has_symbol else "No")
    table.add_row("Repeated Pattern", "Yes" if result.repeated_pattern else "No")
    table.add_row("Sequential Pattern", "Yes" if result.sequential_pattern else "No")
    table.add_row("Found in Local Wordlist", "Yes" if result.in_breach_wordlist else "No")
    table.add_row("Score", str(result.score))
    table.add_row("Strength", result.strength)
    table.add_row("Risk", risk_level)
    table.add_row("Notes", "; ".join(result.notes) if result.notes else "Looks good")

    console.print(table)


def print_demo_audit_results(results: list[DemoAuditResult]) -> None:
    table = Table(title="Demo User Audit Results")
    table.add_column("Username")
    table.add_column("Hash Type")
    table.add_column("Weak Password Detected")
    table.add_column("Matched from Local Demo Wordlist")
    table.add_column("Elapsed (s)")
    table.add_column("Notes")

    for item in results:
        table.add_row(
            item.username,
            item.hash_type,
            "Yes" if item.weak_password_detected else "No",
            "Yes" if item.matched_from_demo_wordlist else "No",
            f"{item.elapsed_seconds:.4f}",
            item.notes,
        )

    console.print(table)


def export_demo_results_csv(path: Path, results: list[DemoAuditResult]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["username", "hash_type", "weak_password_detected", "matched_from_demo_wordlist", "elapsed_seconds", "notes"]
        )
        for item in results:
            writer.writerow(
                [
                    item.username,
                    item.hash_type,
                    item.weak_password_detected,
                    item.matched_from_demo_wordlist,
                    f"{item.elapsed_seconds:.6f}",
                    item.notes,
                ]
            )


def export_demo_results_json(path: Path, results: list[DemoAuditResult]) -> None:
    payload = [item.__dict__ for item in results]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
