.PHONY: install run debug clean lint lint-strict build

install:
	python3 -m pip install --upgrade pip build
	python3 -m pip install flake8 mypy

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

build:
	python3 -m build
	cp dist/mazegen-*.whl dist/mazegen-*.tar.gz .

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
