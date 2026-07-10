# papercuts

Tiny, dependency-free CLI for recording small workflow friction during coding-agent work.

## Install

### From GitHub (recommended — one-liner)

```bash
uv tool install git+https://github.com/MarkKon/papercuts.git
```

### From a local clone

```bash
git clone https://github.com/MarkKon/papercuts.git
uv tool install --editable ./papercuts
```

## Usage

From any Git repository:

```bash
papercut "Unquoted zsh glob caused rg to skip the search"
```

The command appends a timestamped bullet to `PAPERCUTS.md` at the repository root.
Use `--file PATH` when a different output file is intentional.
