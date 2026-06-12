import hashlib
import secrets
import bcrypt


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def make_salt(length: int = 8) -> str:
    return secrets.token_hex(length)


def hash_sha256_unsalted(password: str) -> str:
    return sha256_hex(password)


def hash_sha256_salted(password: str, salt: str) -> str:
    return sha256_hex(password + salt)


def hash_bcrypt(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_sha256_unsalted(password: str, stored_hash: str) -> bool:
    return hash_sha256_unsalted(password) == stored_hash


def verify_sha256_salted(password: str, salt: str, stored_hash: str) -> bool:
    return hash_sha256_salted(password, salt) == stored_hash


def verify_bcrypt(password: str, stored_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
