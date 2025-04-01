# Activate the python virtual environment if it's present *and* you're running
# the terminal in vscode.

https://github.com/astral-sh/uv/issues/9637

```.py
if [ "$TERM_PROGRAM" = "vscode" ]; then
    if [ -d "./.venv" ]; then
        source ./.venv/bin/activate
    fi
fi
```