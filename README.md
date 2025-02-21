# devkit

CLI tool providing convenience scripts for my local development.

### Install devkit as a UV tool

```sh
uv tool install git+https://github.com/joerisner/devkit
```

## Development

### Getting started

This project uses `uv` for managing Python versions, dependencies, and the project's environment. Run the `setup` target to get started with `uv`.

```sh
make setup
```

Once the project is setup with `uv`, create the virtual environment and install dependencies.

```sh
make install
```

See additional `make` targets by viewing the [Makefile](./Makefile) or by running `make help` (or just `make`).

### Using the CLI

Use `uv` to run `devkit` locally.

```sh
uv run devkit --help
```
