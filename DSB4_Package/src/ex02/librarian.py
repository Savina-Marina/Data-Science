#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    venv = os.environ.get("VIRTUAL_ENV")
    if not venv:
        raise RuntimeError("Запусти скрипт из активированной виртуальной среды.")

    if os.path.basename(os.path.normpath(venv)) != "marina":
        raise RuntimeError("Неверная виртуальная среда.")

    req_file = "requirements.in.txt"

    with open(req_file, "w", encoding="utf-8") as f:
        f.write("beautifulsoup4\npytest\n")

    subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], check=True)
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], check=True, text=True, capture_output=True)
    freeze_text = result.stdout.strip()
    print(freeze_text)

    with open("requirements.txt", "w", encoding="utf-8") as final:
        final.write(freeze_text + "\n")

if __name__ == "__main__":
    main()