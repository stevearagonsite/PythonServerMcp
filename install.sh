pyenv install 3.12.2
pyenv local 3.12.2
uv venv
RUN uv pip install -e .
uv sync
