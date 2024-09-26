from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)


START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="🛒 ORDER NOW", callback_data="order"),
     InlineKeyboardButton(text="⚙ Manage Services", callback_data="service")
     ]
])

NEXT_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="Back", callback_data="back")]
])

BACK_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="Back", callback_data="back")]
])

VPS_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="CentOS7", callback_data="centos1"),
     InlineKeyboardButton(text="Centos8", callback_data="centos2")
     ],

    [InlineKeyboardButton(text="Ubuntu22.04", callback_data="ubuntu2"),
     InlineKeyboardButton(text="Ubuntu18.04", callback_data="ubuntu1"),
     InlineKeyboardButton(text="Ubuntu20.04", callback_data="ubuntu1")
     ],

    [
        InlineKeyboardButton(text="Debian12", callback_data="debian3"),
        InlineKeyboardButton(text="Debian10", callback_data="debian1"),
        InlineKeyboardButton(text="Debian11", callback_data="debian2")
    ],

    [
        InlineKeyboardButton(text="AlmaLinux9.1", callback_data="AlmaLinux1"),
        InlineKeyboardButton(text="AlmaLinux9.2", callback_data="AlmaLinux2")
    ]
])

SERVICE_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text='START VPS', callback_data='start'),
     InlineKeyboardButton(text='RESTART VPS', callback_data='restart')
     ],

    [InlineKeyboardButton(text='INSTALL', callback_data='install'),
     InlineKeyboardButton(text='QUIT SERVICE', callback_data='quit')
     ]
])

PLUS_MINUS_KEYBOARD = InlineKeyboardButton([
    [InlineKeyboardButton(text="-", callback_data="minus"),
     InlineKeyboardButton(text="0", callback_data="data"),
     InlineKeyboardButton(text="+", callback_data="plus")
     ]
])

REPLY_KEYBOARD = ReplyKeyboardMarkup([
    ['My Data 📅', 'Refferal Link 🔗'], ['Data 📔', 'Balance 💰']

], resize_keyboard=True, input_field_placeholder='ADD TO CART')

REPLY_KEYBOARD_TEST = ReplyKeyboardMarkup([
    [VPS_KEYBOARD], [PLUS_MINUS_KEYBOARD]

], resize_keyboard=True, input_field_placeholder='ADD TO CART')
