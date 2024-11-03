.PHONY: install
install:
	poetry install
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: shell
shell:
	poetry run python manage.py shell

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: clean
clean:
	rm -rf node_modules/ .ruff_cache/ .pytest_cache/
	find . -type d -name "__pycache__" | xargs rm -rf
