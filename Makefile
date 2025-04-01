install_dependencies:
	uv sync

idx_setup:
	@echo $(shell ls ./venv/bin/activate)
	source ./venv/bin/activate
	pip install -r requirements.txt

clean:
	@rm -ff */__pycache__

run-server:
	python main.py

run-server-debug:
	MCP_DEBUG=1 python main.py

run-server-tcp:
	python main.py --transport tcp --port 8080
