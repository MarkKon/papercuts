# papercuts

Tiny, dependency-free CLI for recording small workflow friction during coding-agent work.

Install it once from this checkout:

```bash
uv tool install --editable /Users/kmark/Documents/Repositories/__tools/papercuts
```

From any Git repository:

```bash
papercut "Unquoted zsh glob caused rg to skip the search"
```

The command appends a timestamped bullet to `PAPERCUTS.md` at the repository root.
Use `--file PATH` when a different output file is intentional.
