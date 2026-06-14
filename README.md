# Developer Environment (DEnv)

## Information

DEnv is a developer environment tool that automatically sets up and manages your development environment without any manual configuration.
It is fully automated and supports multiple programming languages and frameworks. Although it is still under development, it is already a powerful tool for managing your development environment.

## Usage

**Step 1:** Download the latest release from the [GitHub repository](https://github.com/apesta0/denv/releases) and extract the archive.

**Step 2:** Add the extracted directory to your system's PATH.

*2.1* Open your shell configuration file (e.g. `~/.bashrc` or `~/.zshrc`) and add the following line:

```bash
export PATH="$PATH:/path/to/denv"
```

*2.2* Save the file and restart your shell using `source ~/.bashrc` or `source ~/.zshrc`.

**Step 3:** Run `./denv <filetype>` to set up your development environment for the specified filetype.

*3.1* You can also set up the environment for a specific setting using flags, for example `./denv -c -C-All`.


## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/apesta0/denv/issues).

### Submitting a Pull Request

To submit a pull request, please follow these steps:

1. Fork the [GitHub repository](https://github.com/apesta0/denv/fork).

2. Create a new branch for your changes.

3. Make your changes and commit them to your branch.

4. Push your branch to your fork.

5. Open a pull request on the [GitHub repository](https://github.com/apesta0/denv/pulls).

### Starring

If you find this project useful, please consider starring it on [GitHub](https://github.com/apesta0/denv). It is also a form of contribution and recognition for the work done by the project maintainers.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
