#!/usr/bin/env python

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from telegram import __version__ as TG_VER
import logging

import api.ai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BOT_API = os.getenv("BOT_API")

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Nice to meet you.",
        reply_markup=ForceReply(selective=True),
    )
    await help_command(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Reply to my message to get started!")


async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(update.message.text) <= 6:
        await update.message.reply_markdown_v2("Correct syntax to generate an image is,\n`/image a sweet cat is eating a pumpkin`")
    else:
        await update.message.reply_text("Generating an image...")
        ai_reply = api.ai.ai_img_generation(update.message.text[7:], update.message.chat.type)
        await update.message.reply_markdown_v2(f"Here's your [image]({ai_reply})\.")



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    ai_reply_text_message = api.ai.ai_completion(update.message.text, update.message.chat.type).strip("\n")
    await update.message.reply_text(ai_reply_text_message)

    


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_API).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("image", image_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
