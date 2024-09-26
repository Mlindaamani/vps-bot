

# MODULE_1 -> VPS_BOT
from dotenv import load_dotenv
from telegram import Update
from logging_service import Logger
import os
from utilis import send_typing_action
from telegram import Update
from messages import (
    HELP_MESSAGE,
    WELCOME_MESSAGE,
    PROJECT_NAME,
    LIST_TEXT,
)
from keyboards import (
    START_KEYBOARD,
    VPS_KEYBOARD,
    SERVICE_KEYBOARD
)

from telegram.ext import (
    Updater,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)

load_dotenv('.env')
logger = Logger('logs/bot.log')


class TelegramBot:
    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.updater = Updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    @staticmethod
    def start_command(update: Update, context: ContextTypes):
        update.message.reply_text(
            WELCOME_MESSAGE.replace("PROJECTNAME", PROJECT_NAME),
            reply_markup=START_KEYBOARD)
        logger.log_info("Done executing start command")

    @staticmethod
    def help_command(update: Update, context: ContextTypes):
        update.message.reply_text(HELP_MESSAGE)

    @staticmethod
    def inline_query_handlers(update: Update, context: ContextTypes):
        reply_markup = None
        data = update.callback_query.data
        if data == 'order':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                'Choose VPS Below', reply_markup=VPS_KEYBOARD)

        if data == 'service':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                "Choose Service Bellow", reply_markup=SERVICE_KEYBOARD)

        if data == 'start':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                'Starting the the OS....', reply_markup=reply_markup)

        if data == 'restart':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                'Restarting the the OS....', reply_markup=reply_markup)

        if data == 'install':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                'Installing the the OS please wait for few minutes....', reply_markup=reply_markup)

        if data == 'quit':
            update.callback_query.answer()
            update.callback_query.edit_message_text(
                'Deleting your data and quiting.....', reply_markup=reply_markup)

    @send_typing_action
    def message_handler(update: Update, context: ContextTypes):
        """This will respond to only `text`"""
        text = update.message.text.lower()
        if text == "hello":
            TelegramBot.bot_reply(update, "Hello how are doing?")
        elif text in LIST_TEXT:
            TelegramBot.bot_reply(update, "Great! How can i help you")
        else:
            TelegramBot.bot_reply(update, "I don't understand you")

    @staticmethod
    def bot_reply(update: Update, text):
        return update.message.reply_text(text)

    def register_callback_query(self) -> None:
        self.dispatcher.add_handler(
            CallbackQueryHandler(TelegramBot.inline_query_handlers))

    def register_messages(self) -> None:
        self.dispatcher.add_handler(MessageHandler(
            Filters.text & ~Filters.command, TelegramBot.message_handler))

    def register_commands(self) -> None:
        self.dispatcher.add_handler(CommandHandler(
            "start", TelegramBot.start_command))

        self.dispatcher.add_handler(
            CommandHandler("help", TelegramBot.help_command))

    def start_bot(self) -> None:
        """Run  the bot and starting polling"""

        print("VPS BOT started....")
        logger.log_debug('Bot started...')

        self.register_commands()
        self.register_callback_query()
        self.register_messages()
        self.updater.start_polling()

        self.updater.idle()


if __name__ == "__main__":
    bot = TelegramBot()
    bot.start_bot()
