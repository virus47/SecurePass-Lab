import re
from lab.models import PasswordCheckResult


SEQUENTIAL_PATTERNS = [
    "123",
    "234",
    "345",
    "456",
    "567",
    "678",
    "789",
    "abc",
    "bcd",
    "cde",
    "qwerty",
]


def has_repeated_pattern(password: str) -> bool:
    return bool(re.search(r"(.)\1\1", password))


def has_sequential_pattern(password: str) -> bool:
    lowered = password.lower()
    return any(pattern in lowered for pattern in SEQUENTIAL_PATTERNS)


def evaluate_password(password: str, breach_words: set[str]) -> PasswordCheckResult:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    repeated_pattern = has_repeated_pattern(password)
    sequential_pattern = has_sequential_pattern(password)
    in_breach_wordlist = password.lower() in breach_words

    score = 0
    notes: list[str] = []

    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        notes.append("Password is shorter than 8 characters.")

    if has_upper:
        score += 1
    else:
        notes.append("Missing uppercase character.")

    if has_lower:
        score += 1
    else:
        notes.append("Missing lowercase character.")

    if has_digit:
        score += 1
    else:
        notes.append("Missing digit.")

    if has_symbol:
        score += 1
    else:
        notes.append("Missing symbol.")

    if repeated_pattern:
        score -= 2
        notes.append("Contains repeated character pattern.")

    if sequential_pattern:
        score -= 2
        notes.append("Contains common sequential pattern.")

    if in_breach_wordlist:
        score -= 4
        notes.append("Password appears in local breach/common-password wordlist.")

    if score >= 6:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return PasswordCheckResult(
        password=password,
        length=len(password),
        has_upper=has_upper,
        has_lower=has_lower,
        has_digit=has_digit,
        has_symbol=has_symbol,
        repeated_pattern=repeated_pattern,
        sequential_pattern=sequential_pattern,
        in_breach_wordlist=in_breach_wordlist,
        score=score,
        strength=strength,
        notes=notes,
    )
