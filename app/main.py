from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.errors import error_handler
from handlers.base import start_handler
from settings import get_settings
from watchfiles import run_process


def get_app():
    """Sets up and returns the Telegram bot application."""
    settings = get_settings()
    application = ApplicationBuilder().token(settings.TG_BOT_TOKEN).build()

    # Command handler for the /start command
    start_command_handler = CommandHandler('start', start_handler)
    application.add_handler(start_command_handler)
    
    # Uncomment this section to add a message handler in the future
    # message_handler = MessageHandler(
    #     filters=filters.TEXT & ~filters.COMMAND,
    #     callback=your_message_handler,
    # )
    # application.add_handler(message_handler)

    # Error handler to catch and process exceptions
    application.add_error_handler(error_handler, block=True)

    # Start polling to receive updates
    application.run_polling()

def on_reload(changes):
    """Callback executed when the application is reloaded."""
    print(f"\n--- Changes detected: {changes}. Reloading the application... ---\n")



if __name__ == '__main__':
    print("Starting Telegram bot...")
    run_process(
        ".",
        target=get_app,
        callback=on_reload  # Notify when the application reloads
    )
