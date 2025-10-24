from database.database import db

MESSAGES = {
    'ru' : {
        'start' : 'Привет!\nЯ бот-конвертер валют, с помощью меня ты можешь узнать курс всех валют в мире, переконвертировать валюту одной страны в валютуту другой страны и посчитать результаты, потому что дополнительно встроен калькулятор. Ваш язык: {current_language}',
        'help' : 'Помощь:\n 1. Чтобы конвертировать валюту одной страны в валюту другой страны используй команду /convert (число-1) (валюта) (валюта, в которую нужно перевести), где число-1 указывает на количество первой валюты. Сами валюты в обязательном порядке нужно указать в буквах, например USD, для доллара, RUB для рублей и так далее.\n 2. Чтобы получить список курса валют мира в формате JSON, используйте команду /rates\n 3. Чтобы посчитать математическое выражение используйте команду /match (математическое выражение), где в математическом выражении допустимы следующие символы: 1234567890*/()+-. Само математическое выражение необходимо писать слитно, без пробелов, чтобы бот мог кореектно рассчитать само математическое выражение.',
        'rate' : 'Текущий курс относительно USD 📊',
        'convert' : 'Результат перевода валют: {amount} {from_rate} -> {result} {to_rate}',
        'match' : 'Результат: {result}',
        'change_lang' : 'Выберите язык',
        'new_lang' : 'Ваш новый язык: {current_language}',
        'error_sending' : 'Ошибка во время отправки',
        'not_supported' : 'Одна из валют не поддерживается, либо ее не существует.',
        'invalid_command_format' : 'Неверный формат команды.',
        'invalid_data_format' : 'Неверный формат данных.',
        'settings' : '',
    },
    'en' : {
        'start' : 'Hello! I\'m a currency converter bot. With my help, you can find out the exchange rates of all currencies in the world, convert one country\'s currency to another, and calculate the results, thanks to the built-in calculator. Your language: {current_language}',
        'help' : 'Help:\n 1. To convert one country\'s currency to another, use the /convert (number-1) (currency) (currency to convert to) command, where number-1 indicates the amount of the first currency. The currencies themselves must be specified in letters, for example, USD for the dollar, RUB for rubles, and so on.\n 2. To get a list of world currency exchange rates in JSON format, use the /rates command.\n 3. To calculate a mathematical expression, use the /match (math expression) command, where the following characters are allowed in the mathematical expression: 1234567890*/()+-. The mathematical expression itself must be written as one string, without spaces, so that the bot can correctly calculate the mathematical expression.',
        'rate' : 'Current exchange rate against USD 📊',
        'convert' : 'Currency conversion result: {amount} {from_rate} -> {result} {to_rate}',
        'change_lang' : 'Select language',
        'new_lang' : 'Your new language: {current_language}',
        'match' : 'Result: {result}',
        'error_sending' : 'Error during sending',
        'not_supported' : 'One of the currencies is not supported or does not exist.',
        'invalid_command_format' : 'Invalid command format.',
        'invalid_data_format' : 'Invalid data format.',
        'settings' : '',
    }
}

def get_user_language(user_id: int) -> str:
    return db.get_user_language(user_id)

def get_text(user_id: int, text_key: str, **kwargs) -> str:
    lang = get_user_language(user_id)
    text = MESSAGES[lang][text_key]
    return text.format(**kwargs) if kwargs else text