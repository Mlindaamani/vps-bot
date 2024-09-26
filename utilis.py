# DECORATORS-> MODULE
from telegram import Update
from functools import wraps
from telegram import ChatAction, Update, InputMediaPhoto
from telegram.ext import CallbackContext
import telegram
from functools import wraps
import time
media1 = InputMediaPhoto(media=open('images/math_image.png', 'rb'))

media2 = InputMediaPhoto(media=open('images/image.png', 'rb'))

MEDIA_LIST = [media1, media2]

LIST_OF_ADMINS = [1740888476, 87654321]


def restricted(function):
    """This decorator will restrict access to the functon decorated by this decorator"""
    @wraps(function)
    def wrapper(update: Update, context: CallbackContext):
        if update.effective_user.id not in LIST_OF_ADMINS:
            update.message.reply_text(
                "<i>Access denied. You must be an Admin</i> ", parse_mode=telegram.ParseMode.HTML)
            return
        return function(update, context)
    return wrapper


def send_typing_action(function):
    """Send `typing...` while processing `function`"""
    @wraps(function)
    def wrapper(update: Update, context: CallbackContext):
        update.message.reply_chat_action(ChatAction.TYPING)
        return function(update, context)
    return wrapper


def send_recording_video_note_action(function):
    """Send `recoding video note...` while processing `'function'` """
    @wraps(function)
    def wrapper(update: Update, context: CallbackContext):
        update.message.reply_chat_action(action=ChatAction.RECORD_VIDEO_NOTE)
        return function(update, context)
    return wrapper


def send_action(action):
    """Send `'action...'` while processing `'function'`"""

    def decorator(function):
        @wraps(function)
        def wrapper(update: Update, context: CallbackContext):
            update.message.reply_chat_action(action=action)
            return function(update, context)
        return wrapper
    return decorator


def send_captcha_command(update: Update, context: CallbackContext):
    """Type `/captcha` to send captcha"""
    update.message.reply_photo(photo=open('images/math_image.png', 'rb'),
                               caption="Solve the Captcha to continue")
    update.message.reply_media_group(media=MEDIA_LIST)


def measure_execution_time(function):
    @wraps(function)
    def wrapper():
        start_time = time.perf_counter
        result = function()
        end_time = time.perf_counter
        execution_time = end_time - start_time
        print(f"""Time taken: {execution_time:.2f} seconds""")
        return result
    return wrapper
