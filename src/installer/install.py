#!/usr/bin/env python3

import os
import shutil
import stat
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

ROOT_DIR = Path(__file__).resolve().parents[2]

DEFAULT_INSTALL_DIR = Path.home() / ".local" / "share" / "denv"
DEFAULT_BIN_DIR = Path.home() / ".local" / "bin"


def detect_shell():
    return os.path.basename(os.environ.get("SHELL", ""))


def get_shell_config(shell):
    configs = {
        "bash": Path.home() / ".bashrc",
        "zsh": Path.home() / ".zshrc",
        "fish": Path.home() / ".config" / "fish" / "config.fish",
    }

    return configs.get(shell)


def add_path_entry(bin_dir):
    shell = detect_shell()
    config = get_shell_config(shell)

    if config is None:
        return

    config.parent.mkdir(parents=True, exist_ok=True)

    if shell == "fish":
        entry = f"fish_add_path {bin_dir}"
    else:
        entry = f'export PATH="{bin_dir}:$PATH"'

    if config.exists():
        content = config.read_text()

        if entry in content:
            return

    with open(config, "a") as f:
        f.write("\n# DEnv\n")
        f.write(entry + "\n")


def create_launcher(install_dir, bin_dir):
    bin_dir.mkdir(parents=True, exist_ok=True)

    launcher = bin_dir / "denv"

    launcher.write_text(
        f"""#!/bin/bash
python3 "{install_dir / "src" / "denv.py"}" "$@"
"""
    )

    launcher.chmod(launcher.stat().st_mode | stat.S_IEXEC)


def install(install_dir):
    install_dir = Path(install_dir)
    bin_dir = DEFAULT_BIN_DIR

    if install_dir.exists():
        shutil.rmtree(install_dir)

    install_dir.mkdir(parents=True)

    for item in ROOT_DIR.iterdir():
        if item.name == ".git":
            continue

        destination = install_dir / item.name

        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    create_launcher(install_dir, bin_dir)

    add_path_entry(bin_dir)

    return install_dir


class InstallerGUI:
    def __init__(self, root):
        self.root = root

        root.title("DEnv Installer")
        root.geometry("650x300")

        tk.Label(root, text="DEnv Installer", font=("Arial", 18, "bold")).pack(pady=10)

        self.shell = detect_shell()

        tk.Label(root, text=f"Detected shell: {self.shell}").pack()

        frame = tk.Frame(root)
        frame.pack(fill="x", padx=20, pady=20)

        tk.Label(frame, text="Install Location:").pack(anchor="w")

        self.install_path = tk.StringVar(value=str(DEFAULT_INSTALL_DIR))

        tk.Entry(frame, textvariable=self.install_path, width=70).pack(
            side="left", fill="x", expand=True
        )

        tk.Button(frame, text="Browse", command=self.browse).pack(side="left", padx=5)

        self.status = tk.Label(root, text="Ready")

        self.status.pack(pady=10)

        tk.Button(
            root, text="Install", command=self.run_install, height=2, width=20
        ).pack()

    def browse(self):
        path = filedialog.askdirectory()

        if path:
            self.install_path.set(path)

    def run_install(self):
        try:
            self.status.config(text="Installing...")

            install(self.install_path.get())

            self.status.config(text="Installation completed.")

            messagebox.showinfo(
                "Success",
                ("DEnv installed successfully.\n\nYou may need to restart your shell."),
            )

        except Exception as e:
            messagebox.showerror("Installation Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    InstallerGUI(root)
    root.mainloop()
