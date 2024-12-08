DC = docker compose
BOT_APP = docker_compose/bot.yaml
ENV = --env-file .env
PP = poetry run python
MAIN = app/main.py

.PHONY: bot-dev
bot-dev:
	$(PP) $(MAIN)

.PHONY: up
up:
	${DC} -f ${BOT_APP} ${ENV} up --build -d

.PHONY: down
down:
	${DC} -f ${BOT_APP} ${ENV} down -v

.PHONY: logs
logs:
	${DC} -f ${BOT_APP} logs -f

.PHONY: bot
bot:
	${DC} -f ${BOT_APP} ${ENV} up --build -d

.PHONY: bot-down
bot-down:
	${DC} -f ${BOT_APP} ${ENV} down

.PHONY: bot-logs
bot-logs:
	${DC} -f ${BOT_APP} logs -f