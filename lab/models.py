from dataclasses import dataclass
from typing import Optional


@dataclass
class DemoUser:
    username: str
    password_hash: str
    hash_type: str
    salt: Optional[str] = None
    strength_label: Optional[str] = None


@dataclass
class PasswordCheckResult:
    password: str
    length: int
    has_upper: bool
    has_lower: bool
    has_digit: bool
    has_symbol: bool
    repeated_pattern: bool
    sequential_pattern: bool
    in_breach_wordlist: bool
    score: int
    strength: str
    notes: list[str]


@dataclass
class DemoAuditResult:
    username: str
    hash_type: str
    weak_password_detected: bool
    matched_from_demo_wordlist: bool
    elapsed_seconds: float
    notes: str
