from config import OUTPUT_DIR
from lab.cli import build_parser
from lab.engine import (
    run_audit_demo_users_mode,
    run_breach_check_mode,
    run_check_password_mode,
    run_generate_mode,
)
from lab.utils import ensure_directories


def main() -> None:
    ensure_directories([OUTPUT_DIR])
    parser = build_parser()
    args = parser.parse_args()

    if args.mode == "generate":
        run_generate_mode(args)
    elif args.mode == "audit-demo-users":
        run_audit_demo_users_mode(args)
    elif args.mode == "check-password":
        run_check_password_mode(args)
    elif args.mode == "breach-list-check":
        run_breach_check_mode(args)
    else:
        parser.error("Unsupported mode.")


if __name__ == "__main__":
    main()
