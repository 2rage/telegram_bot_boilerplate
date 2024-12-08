# Telegram Bot Boilerplate

A flexible boilerplate for building Telegram bots using modern tools and best practices. This project is designed to simplify the setup, development, and scaling of Telegram bots, with support for both development and production environments

---

## Features

- **Python 3.12+**: Built with the latest Python features
- **Telegram Bot API**: Powered by `python-telegram-bot`
- **Auto-Reload**: Supports auto-reloading during development using `watchfiles`
- **Environment Configuration**: Easy setup with `.env` file
- **Docker Support**: Ready for containerized deployments
- **Makefile**: Simplified commands for common tasks
- **Clean Structure**: Modular and scalable architecture for adding features

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.12+**: [Download Python](https://www.python.org/downloads/)
- **Poetry**: For dependency management ([Install Poetry](https://python-poetry.org/docs/#installation))
- **Docker** (optional): For running the bot in a container

---

## Installation

1. **Clone the repository**:

Replace `YOUR_APP_NAME` with your desired project name

```bash
git clone https://github.com/2rage/telegram_bot_boilerplate.git
mv telegram_bot_boilerplate YOUR_APP_NAME
cd YOUR_APP_NAME
```

2. **Removing Git History**:

```bash
rm -rf .git
git init
```

3. **Set up environment variables**:
- Create a .env file by copying the example:

    ```bash
    cp .env.example .env && rm .env.example
    ```

- Edit the `.env` file and add your configuration

4. **Install dependencies**:

```bash
poetry install
```

5. **Run the bot**

```bash
make bot-dev
```

## Project Structure

```
├── Dockerfile                 # Docker image setup
├── Makefile                   # Simplified automation commands
├── README.md                  # Project documentation
├── app/                       # Main application folder
│   ├── exceptions/            # Custom exception classes
│   │   └── base.py            # Base application exception
│   ├── handlers/              # Command and message handlers
│   │   ├── base.py            # Basic command handlers (e.g., /start)
│   │   └── errors.py          # Error handling logic
│   ├── main.py                # Entry point for the bot
│   └── settings.py            # Configuration and environment variables
├── docker_compose/            # Docker Compose configuration
│   └── bot.yaml               # Configuration for running the bot container
├── poetry.lock                # Poetry lock file
└── pyproject.toml             # Poetry configuration
```
