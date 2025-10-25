from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from languages.languages import get_user_language

def get_language_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text = 'Русский 🇷🇺', callback_data = 'lang_ru')
    builder.button(text = 'English 🇬🇧', callback_data = 'lang_en')
    builder.adjust(2)
    return builder.as_markup()

def get_main_keyboard(user_id: int):
    lang = get_user_language(user_id)
    builder = InlineKeyboardBuilder()

    if lang == 'en':
        builder.button(text = '📖 Help', callback_data = 'help')
        builder.button(text = '📈 Rate', callback_data = 'rate')
        builder.button(text = '📊 My profile', callback_data = 'my_profile')
    
    else:
        builder.button(text = '📖 Помощь', callback_data = 'help')
        builder.button(text = '📈 Курс', callback_data = 'rate')
        builder.button(text = '📊 Мой профиль', callback_data = 'my_profile')
    
    builder.adjust(1)
    return builder.as_markup()