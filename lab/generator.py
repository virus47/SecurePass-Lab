from config import DEMO_USERS_FILE
from lab.hashing import hash_bcrypt, hash_sha256_salted, hash_sha256_unsalted, make_salt
from lab.utils import save_json


WEAK_PASSWORDS = [
    "123456",
    "password",
    "qwerty123",
    "welcome1",
    "admin123",
]

MEDIUM_PASSWORDS = [
    "Welcome123",
    "Secure2024",
    "Python_User7",
]

STRONG_PASSWORDS = [
    "R!verStone#29",
    "T!gerMoon$481",
    "Aster@Code9*X",
]


def generate_demo_users(count: int) -> list[dict]:
    users: list[dict] = []
    password_pool = WEAK_PASSWORDS + MEDIUM_PASSWORDS + STRONG_PASSWORDS
    hash_types = ["sha256_unsalted", "sha256_salted", "bcrypt"]

    for i in range(count):
        username = f"user_{i+1:02d}"
        password = password_pool[i % len(password_pool)]
        hash_type = hash_types[i % len(hash_types)]

        if hash_type == "sha256_unsalted":
            user = {
                "username": username,
                "password_hash": hash_sha256_unsalted(password),
                "hash_type": hash_type,
                "salt": None,
                "strength_label": None,
            }
        elif hash_type == "sha256_salted":
            salt = make_salt()
            user = {
                "username": username,
                "password_hash": hash_sha256_salted(password, salt),
                "hash_type": hash_type,
                "salt": salt,
                "strength_label": None,
            }
        else:
            user = {
                "username": username,
                "password_hash": hash_bcrypt(password),
                "hash_type": hash_type,
                "salt": None,
                "strength_label": None,
            }

        users.append(user)

    save_json(DEMO_USERS_FILE, users)
    return users
