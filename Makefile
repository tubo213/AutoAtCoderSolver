.PHONY: format lint set-template

# ruffでフォーマットを行う
format:
	rye run ruff format

# ruffでlintとフォーマットを行う
lint:
	rye run ruff check --fix; rye run mypy . --config-file pyproject.toml

# テンプレートを設定する
set-template:
	cp -r template.json `acc config-dir`/python/template.json
	acc config default-template python