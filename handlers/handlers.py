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
    await message.answer('<b>ConverterBot v1</b> by @ghostfaccee\n Доступные команды:\n  ├── /start - старт бота\n  ├── /help - помощь\n  ├── /rate - текущий курс валют относительно USD\n  └── /match - математический калькулятор', parse_mode=ParseMode.HTML)

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
        print(e)
        await message.answer('Ошибка во время отправки файла')

@router.message(Command('match'))
async def cmd_match(message: Message) -> None:
    await message.reply('match...')