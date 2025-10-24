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
    await callback.answer()
    user_id = callback.from_user.id
    text = get_text(user_id, 'help')
    await callback.message.answer(text)

@router.callback_query(F.data == 'rate')
async def callback_rate(callback: CallbackQuery) -> None:
    await callback.answer()
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
    
    await callback.message.edit_text(text, reply_markup=get_main_keyboard(user_id))

@router.message(Command('convert'))
async def cmd_convert(message: Message) -> None:
    user_id = message.from_user.id
    try:
        parts = message.text.split()
        if len(parts) != 4:
            invalid_format = get_text(user_id, 'invalid_command_format')
            await message.answer(invalid_format)
            return
        try:
            amount = float(parts[1])
            from_rate = parts[2].upper()
            to_rate = parts[3].upper()
        except Exception:
            invalid_format = get_text(user_id, 'invalid_data_format')
            await message.answer(invalid_format)
            return
        data = await api_requests.get_exchage_rate()
        if from_rate not in data['conversion_rates'] or to_rate not in data['conversion_rates']:
            not_supported = get_text(user_id, 'not_supported')
            await message.answer(not_supported)
            return
        from_rate_currency = (data['conversion_rates'][from_rate])
        to_rate_currency = (data['conversion_rates'][to_rate])
        result = str((amount / from_rate_currency) * to_rate_currency)
        text = get_text(user_id, 'convert', amount = amount, from_rate = from_rate, result = result, to_rate = to_rate)
        await message.answer(text)
    except Exception:
        error = get_text(user_id, 'error_sending')
        await message.answer(error)

@router.message(Command('match'))
async def cmd_match(message: Message) -> None:
    user_id = message.from_user.id
    try:
        allowed_chars = set('1234567890*/()+-.')
        text = message.text.strip().split()
        calc = text[1]
        if len(text) > 2:
            invalid_format = get_text(user_id, 'invalid_command_format')
            await message.answer(invalid_format)
            return
        if all(char in allowed_chars for char in calc) and text:
            result = eval(calc)
            text = get_text(user_id, 'match', result = result)
            await message.answer(text)
            return
        else:
            invalid_format = get_text(user_id, 'invalid_command_format')
            await message.answer(invalid_format)
            return
    except Exception:
        error_sending = get_text(user_id, 'error_sending')
        await message.answer(error_sending)

@router.callback_query(F.data == 'my_profile')
async def callback_profile(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    language = get_user_language(user_id)
    text = get_text(user_id, 'profile', id = user_id, language = language)
    await callback.message.answer(text)