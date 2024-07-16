include .env
export
DOCKER_COMPOSE := $(shell command -v docker-compose > /dev/null 2>&1 && echo docker-compose || echo docker compose)

.PHONY: lint
lint:
	poetry run black .
	poetry run isort .
	cd src && poetry run flake8 .

.PHONY: setup
setup:
	pip install --upgrade pip==$(PIP_VERSION)
	pip install --upgrade poetry==$(POETRY_VERSION)
	poetry env use $(PYTHON_VERSION)
	poetry install

.PHONY: run-server
run-server:
	poetry run uvicorn user_management.main:app --host 0.0.0.0 --port 5000

.PHONY: db-migrate
db-migrate:
	poetry run alembic upgrade head

.PHONY: run-tests
run-tests:
	poetry run pytest -s

.PHONY: docker-lint
docker-lint:
	$(DOCKER_COMPOSE) run --rm webapp sh -c "flake8 && black . && isort ."

.PHONY: docker-lint
docker-build:
	$(DOCKER_COMPOSE) build --no-cache

.PHONY: docker-up
docker-up:
	$(DOCKER_COMPOSE) up --detach --remove-orphans

.PHONY: docker-db-migrate
docker-db-migrate:
	$(DOCKER_COMPOSE) exec webapp alembic upgrade head

.PHONY: docker-down
docker-down:
	$(DOCKER_COMPOSE) down --remove-orphans

.PHONY: clean
docker-clean:
	$(DOCKER_COMPOSE) down --remove-orphans
	rm -rf .local/services
	rm -rf .pytest_cache
