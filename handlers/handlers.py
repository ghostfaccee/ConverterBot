from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import Router, F
from aiogram.enums import ParseMode


from utils import api_requests
from languages.languages import get_user_language, get_text
from keyboards.keyboards import get_main_keyboard, get_language_keyboard
from database.database import db

import datetime
import json

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    user_id = message.from_user.id
    current_language = get_user_language(user_id)
    text = get_text(user_id, 'start', current_language = current_language)
    await message.answer(text, reply_markup = get_main_keyboard(user_id))

@router.callback_query(F.data == 'help')
async def callback_help(callback: CallbackQuery) -> None:
    callback.answer()
    user_id = callback.from_user.id
    text = get_text(user_id, 'help')
    await callback.message.answer(text)

@router.callback_query(F.data == 'rate')
async def callback_rate(callback: CallbackQuery) -> None:
    callback.answer()
    user_id = callback.from_user.id
    try:
        data = await api_requests.get_exchage_rate()
        filename = f'exchange_{datetime.datetime.now()}.json'
        with open(filename, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent = 2, ensure_ascii = False)
        file = FSInputFile(filename)
        success_text = get_text(user_id, 'rate')
        await callback.message.answer_document(file, caption=success_text)
    except Exception as e:
        error_text = get_text(user_id, 'error_sending')
        await callback.message.answer(error_text)


@router.message(Command('language'))
async def cmd_language(message: Message) -> None:
    user_id = message.from_user.id
    text = get_text(user_id, 'change_lang')
    await message.answer(text, reply_markup=get_language_keyboard())

@router.callback_query(F.data.startswith("lang_"))
async def change_language(callback: CallbackQuery):
    user_id = callback.from_user.id
    language = callback.data.split("_")[1]
    db.update_user_language(user_id, language)
    current_language = get_user_language(user_id)
    text = get_text(user_id, 'new_lang', current_language = current_language)
    
    await callback.message.edit_text(text, reply_markup=get_main_keyboard(user_id)
    )

@router.message(Command('convert'))
async def cmd_convert(message: Message) -> None:
    try:
        parts = message.text.split()
        if len(parts) != 4:
            await message.answer('Неверный формат команды. Подробнее: /help')
            return
        try:
            amount = float(parts[1])
            from_rate = parts[2].upper()
            to_rate = parts[3].upper()
        except Exception:
            await message.answer('Данные указаны не в том формате. Подробнее: /help')
            return
        data = await api_requests.get_exchage_rate()
        if from_rate not in data['conversion_rates'] or to_rate not in data['conversion_rates']:
            await message.answer('Одна из валют не поддерживается. Подробнее: /help')
            return
        from_rate_currency = (data['conversion_rates'][from_rate])
        to_rate_currency = (data['conversion_rates'][to_rate])
        result = str((amount / from_rate_currency) * to_rate_currency)
        await message.answer(result)
    except Exception as e:
        print(e)
        await message.answer('Ошибка во время отправки сообщения')

@router.message(Command('match'))
async def cmd_match(message: Message) -> None:
    try:
        allowed_chars = set('1234567890*/()+-.')
        text = message.text.strip().split()
        calc = text[1]
        if len(text) > 2:
            await message.answer('Неверный формат команды. Подробнее: /help')
            return
        if all(char in allowed_chars for char in calc) and text:
            result = eval(calc)
            await message.answer(f'Результат: {result}')
            return
        else:
            await message.answer('Неверный формат команды. Подробнее: /help')
            return
    except Exception as e:
        await message.answer('Ошибка во время отправки сообщения.')