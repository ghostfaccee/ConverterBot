from database.database import db

MESSAGES = {
    'ru' : {
        'start' : '👋 <b>Привет!</b>\n<i>RatesFlow — это бот-конвертер валют, который позволяет вам узнавать курсы обмена всех валют мира, конвертировать валюту одной страны в валюту другой и рассчитывать результаты.</i>\n<b>Ваш язык:</b> {current_language}\n<b>Разработчик:</b> @ghostfaccee',
        'help' : '📋 <b>Помощь:</b>\n <b>1.</b> <i>Чтобы конвертировать валюту одной страны в валюту другой страны используйте команду /convert (число-1) (валюта) (валюта, в которую нужно перевести), где число-1 указывает на количество первой валюты. Сами валюты в обязательном порядке нужно указать в буквах, например USD, для доллара, RUB для рублей и так далее. Чтобы подробнее узнать о поддерживаемых валютах, советуем вам просмотреть</i> <a href="https://github.com/ghostfaccee/RatesFlow/tree/main/docs">оффициальную документацию проекта RatesFlow</a>. \n <b>2.</b> <i>Чтобы сменить язык пользователя, используйте команду /language.</i> \n <b>3.</b> <i>Чтобы просмотреть курс валют, информацию о пользователе или помощь, используйте команду /start и функции, которые она вам предоставит.</i> \n <b>4.</b> <i>Если все же возникли вопросы по поводу использования телеграм-бота RatesFlow, рекомендуем обратиться вам к</i> <a href="https://github.com/ghostfaccee/RatesFlow/tree/main/docs">оффициальной документации проекта</a>.',
        'rate' : '📊 <b>Текущий курс относительно USD</b>',
        'convert' : '🔄 <b>Результат перевода валют:</b> <i>{amount} {from_rate} -> {result} {to_rate}</i>',
        'match' : '<b>Результат:</b> <i>{result}</i>',
        'change_lang' : '↔️ <b>Выберите язык</b>',
        'new_lang' : '<b>Ваш новый язык:</b> <i>{current_language}</i>',
        'error_sending' : '❌ Ошибка во время отправки',
        'not_supported' : '❌ Одна из валют не поддерживается, либо ее не существует.',
        'invalid_command_format' : '❌ Неверный формат команды.',
        'invalid_data_format' : '❌ Неверный формат данных.',
        'profile' : '🪪 <b>Ваш профиль:</b>\n <b>Ваш ID:</b> <tg-spoiler>{id}</tg-spoiler>\n <b>Ваш язык:</b> <i>{language}</i>',
    },
    'en' : {
        'start' : '👋 <b>Hello!</b>\n<i>RatesFlow is a currency converter bot that allows you to find exchange rates for all currencies in the world, convert one country\'s currency to another, and calculate the results.</i>\n<b>Your language:</b> {current_language}\n<b>Developer:</b> @ghostfaccee',
        'help' : '📋 <b>Help:</b>\n <b>1.</b> <i>To convert the currency of one country to the currency of another, use the command /convert (number-1) (currency) (currency to convert to), where number-1 indicates the amount of the first currency. The currencies themselves must be specified in letters, for example, USD for the dollar, RUB for rubles, and so on. For more information on supported currencies, we recommend viewing</i> <a href="https://github.com/ghostfaccee/RatesFlow/tree/main/docs">the official RatesFlow project documentation.</a> \n <b>2.</b> <i>To change the user\'s language, use the /language command.</i> \n <b>3.</b> <i>To view exchange rates, user information, or help, use the /start command and the functions it provides.</i> \n <b>4.</b> <i>If you still have questions about using the RatesFlow Telegram bot, we recommend that you refer to the</i> <a href="https://github.com/ghostfaccee/RatesFlow/tree/main/docs">official project documentation</a>.',
        'rate' : '📊 <b>Current exchange rate against USD</b>',
        'convert' : '🔄 <b>Currency conversion result:</b> <i>{amount} {from_rate} -> {result} {to_rate}</i>',
        'change_lang' : '↔️ <b>Select language</b>',
        'new_lang' : '<b>Your new language:</b> <i>{current_language}</i>',
        'match' : '<b>Result:</b> <i>{result}</i>',
        'error_sending' : '❌ Error during sending',
        'not_supported' : '❌ One of the currencies is not supported or does not exist.',
        'invalid_command_format' : '❌ Invalid command format.',
        'invalid_data_format' : '❌ Invalid data format.',
        'profile' : '🪪 <b>Your profile:</b>\n <b>Your ID:</b> <tg-spoiler>{id}</tg-spoiler>\n <b>Your language:</b> <i>{language}</i>',
    }
}

def get_user_language(user_id: int) -> str:
    return db.get_user_language(user_id)

def get_text(user_id: int, text_key: str, **kwargs) -> str:
    lang = get_user_language(user_id)
    text = MESSAGES[lang][text_key]
    return text.format(**kwargs) if kwargs else text