#!/usr/bin/env python3

import os
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

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


def remove_path_entry():
    shell = detect_shell()
    config = get_shell_config(shell)

    if config is None or not config.exists():
        return

    lines = config.read_text().splitlines()

    filtered = []

    for line in lines:
        if "DEnv" in line:
            continue

        if ".local/bin" in line:
            continue

        if "fish_add_path" in line:
            continue

        filtered.append(line)

    config.write_text("\n".join(filtered) + "\n")


def uninstall(install_dir):
    install_dir = Path(install_dir)

    launcher = DEFAULT_BIN_DIR / "denv"

    if launcher.exists():
        launcher.unlink()

    if install_dir.exists():
        shutil.rmtree(install_dir)

    remove_path_entry()


class UninstallerGUI:
    def __init__(self, root):
        self.root = root

        root.title("DEnv Uninstaller")
        root.geometry("650x250")

        tk.Label(root, text="DEnv Uninstaller", font=("Arial", 18, "bold")).pack(
            pady=10
        )

        self.path_var = tk.StringVar(value=str(DEFAULT_INSTALL_DIR))

        tk.Label(root, text="Install Location:").pack()

        tk.Entry(root, textvariable=self.path_var, width=80).pack(padx=20)

        tk.Button(
            root, text="Remove DEnv", command=self.run_uninstall, height=2, width=20
        ).pack(pady=20)

    def run_uninstall(self):
        result = messagebox.askyesno("Confirm", "Remove DEnv?")

        if not result:
            return

        try:
            uninstall(self.path_var.get())

            messagebox.showinfo("Success", "DEnv removed successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    UninstallerGUI(root)
    root.mainloop()
