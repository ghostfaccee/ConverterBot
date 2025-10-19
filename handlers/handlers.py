from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram import Router, F
from aiogram.enums import ParseMode


from utils import api_requests

import datetime
import json

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer('<b>ConverterBot v1</b> by @ghostfaccee\n Доступные команды:\n  ├── /start - запуск бота\n  ├── /help - помощь\n  ├── /rate - текущий курс валют относительно USD\n  └── /match - математический калькулятор', parse_mode=ParseMode.HTML)

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.reply('help....')

@router.message(Command('rate'))
async def cmd_rate(message: Message) -> None:
    try:
        data = await api_requests.get_exchage_rate()
        filename = f'exchange_{datetime.datetime.now()}.json'
        with open(filename, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent = 2, ensure_ascii = False)
        file = FSInputFile(filename)
        await message.answer_document(file, caption='Текущий курс относительно USD 📊')
    except Exception as e:
        await message.answer('Ошибка во время отправки файла')

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
    await message.reply('match...')