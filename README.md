# SecurePass Lab

SecurePass Lab is an offline password health, exposure, and demo audit toolkit for local educational use.

## Features
- Password health check
- Local breach/common-password wordlist check
- Demo user dataset generation
- Demo user offline audit mode
- Live terminal progress
- CSV and JSON export
- Linux and Termux-friendly CLI

## Modes

### Generate demo users
```bash
python3 run.py --mode generate --users 12

### Audit demo users
```bash
python3 run.py --mode audit-demo-users --delay 20

### Check a password
```bash
python3 run.py --mode check-password --password "Welcome123"

### Check a password again local wordlist
```bash
python3 run.py --mode breach-list-check --password "123456"

### Setup on Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 run.py --mode generate --users 12
python3 run.py --mode audit-demo-users


### Setup on Termux
```bash
pkg update
pkg install python
pip install -r requirements.txt
python3 run.py --mode generate --users 12
python3 run.py --mode check-password


### Safety - This project is for offline defensive education and local dummy/demo data only.
```bash

---

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 run.py --mode generate --users 12
python3 run.py --mode audit-demo-users --delay 20
python3 run.py --mode check-password --password "Welcome123"
python3 run.py --mode breach-list-check --password "123456"


**IF YOU WANT TO ADD CUSTOM WORDLIST YOU CAN ALSO DO SO BY ADDING YOUR WORDLIST IN "securepass-lab/data/wordlists/" DIRECTORY.**
