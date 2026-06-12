from lab.models import PasswordCheckResult


def classify_risk(result: PasswordCheckResult) -> str:
    if result.in_breach_wordlist or result.strength == "Weak":
        return "High"
    if result.strength == "Moderate":
        return "Medium"
    return "Low"
