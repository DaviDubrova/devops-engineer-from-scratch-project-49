install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build --out-dir dist

package-install:
	uv tool install dist/*.whl
