import argparse
from config import DEFAULT_DELAY_MS, DEFAULT_USERS_TO_GENERATE


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="securepass_lab",
        description="Offline password health, exposure, and demo audit toolkit.",
    )

    parser.add_argument(
        "--mode",
        required=True,
        choices=[
            "generate",
            "audit-demo-users",
            "check-password",
            "breach-list-check",
        ],
        help="Mode to run.",
    )

    parser.add_argument(
        "--users",
        type=int,
        default=DEFAULT_USERS_TO_GENERATE,
        help="Number of demo users to generate.",
    )

    parser.add_argument(
        "--delay",
        type=int,
        default=DEFAULT_DELAY_MS,
        help="Artificial delay in milliseconds for demo progress.",
    )

    parser.add_argument(
        "--password",
        type=str,
        help="Password to check in non-interactive mode.",
    )

    return parser
