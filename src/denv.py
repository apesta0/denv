#!/usr/bin/env python3

import shutil
import sys
from pathlib import Path

VERSION = "1.1.0"

BASE_DIR = Path(__file__).resolve().parent


def generate_from_template(template_name):
    template_dir = BASE_DIR / "templates" / template_name

    if not template_dir.exists():
        print(f"Template '{template_name}' not found.")
        print(f"Expected: {template_dir}")
        return False

    for item in template_dir.iterdir():
        destination = Path.cwd() / item.name

        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)

    return True


def replace_placeholders():
    project_name = Path.cwd().name

    for file in Path.cwd().rglob("*"):
        if not file.is_file():
            continue

        try:
            content = file.read_text(encoding="utf-8")

            content = content.replace("{PROJECT_NAME}", project_name)

            file.write_text(content, encoding="utf-8")

        except Exception:
            pass


if len(sys.argv) < 2:
    print("Usage: denv <typefile> <option>")
    sys.exit(1)

lang = sys.argv[1]
option = sys.argv[2] if len(sys.argv) > 2 else None

if lang in ("-v", "-version"):
    print(f"DEnv version {VERSION}\nCopyright (C) 2026 Alex Pesta")

elif lang in ("-as", "-asharp"):
    if generate_from_template("asharp/default"):
        replace_placeholders()

elif lang == "-c":
    if option == "-C-All":
        if generate_from_template("c/all"):
            replace_placeholders()
    else:
        if generate_from_template("c/default"):
            replace_placeholders()

elif lang in ("-cpp", "-c++"):
    if option == "-CPP-All":
        if generate_from_template("cpp/all"):
            replace_placeholders()
    else:
        if generate_from_template("cpp/default"):
            replace_placeholders()

elif lang in ("-py", "-python"):
    if option == "-no-pycache":
        if generate_from_template("python/nopycache"):
            replace_placeholders()
    else:
        if generate_from_template("python/default"):
            replace_placeholders()

elif lang in ("-cs", "-csharp"):
    if generate_from_template("csharp/default"):
        replace_placeholders()

elif lang == "-java":
    if generate_from_template("java/default"):
        replace_placeholders()

else:
    print(f"Unknown language: {lang}")
