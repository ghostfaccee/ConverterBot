# Official RatesFlow Project Documentation
## Introduction
**RatesFlow is a Telegram bot that uses the ExchangeRate API to retrieve exchange rates, convert them, and send the results to the user**

### Project Structure

#### Missing Files in the Open Source Version
Some project files are hidden from the user for security reasons. The bot won't run without them. However, if you're keen to create something similar, the missing files in the open source release are listed below so you can replicate the process.

1. **.env** - This file stores API keys for requests to Telegram and the ExchangeRate API. You can see an example of its formatting in the .env_example file.

#### Project Structure: Directories
* **database/** - Database and its initialization.
* **docs/** - Documentation in Russian and English.
* **handlers/** - Handlers.
* **keyboards/** - Keyboards.
* **languages/** - Functions for switching languages ​​and text in different languages.
* **utils/** - Project utilities. Sending API requests to the ExchangeRate-API.
* **bot.py** - The main project file. This is the file from which the project must be launched.
* **config.py** - Project configurations.
* **log.py** - Project update and change log.
* **LICENSE** - Project license.
* **README.md** - Main project documentation.
* **requirements.txt** - Project dependencies.

## Frequently Asked Questions | FAQ
- **In what format should I request a currency conversion?**
The conversion function works with the command: ```/convert <amount> <cur-1> <cur-2>```, where <amount> is a number with a trailing period (i.e., a comma) and specifies the amount of <cur-1>, which is the currency to be converted to <cur-2>, the desired currency. Incorrectly formatting the command will result in the bot not returning the currency conversion result.

- **Why can I only get the exchange rate in a .json file?**
The maximum length of Telegram messages is 4096. To avoid unnecessary errors with function usage and poor formatting, we decided to simply send users a .json file, which is provided by the ExchangeRate-API. You can also use the /convert command to get the exchange rate against the dollar, where you specify 1 instead of amount.

- **Why do I get a positive response when I enter a negative <amount> in the /convert command?**
Obviously, negative currency values ​​don't exist. Therefore, to avoid errors and incorrect answers, the bot immediately takes the absolute value of the <amount> when it receives it and gets the correct answer.

- **How ​​do I change the language?**
To change the language, use the /language command, and you will be offered several language options.

- **How ​​do I get profile statistics, exchange rates, and help documentation?**
Use the /start command, and you will be offered all these functions.

- **How ​​do I use the calculator provided by the bot?**
To use the calculator, enter the command `/match <math expression>`, where the valid characters in the mathematical expression are as follows:
<1234567890*/()+-.> (angle brackets do not count). The mathematical expression must be a single line, meaning it must not contain spaces. For example, the command `/match 2*2` will be considered valid, while the command `/match 2 * 2` will be invalid. Pay close attention to the number of spaces and characters, otherwise you will not receive a response.

- **What currencies are supported?**
You can find a list of currencies supported by the API, and therefore the bot, at [link](https://www.exchangerate-api.com/docs/supported-currencies).

## Launching the Bot
To launch the bot, you need to create a .env file and place the Telegram bot API and ExchangeRate in it, just as shown in the .env_example file, which is located in the project root. The .env file itself must be created in the same location.

**!-- The instructions below only work on Debian-based Linux distributions (Ubuntu, Mint, Debian, etc.) --!**

1. Create a virtual environment with the command `python3 -m venv .venv` in the terminal.
2. Run the virtual environment `source .venv/bin/activate`.
3. Install dependencies `pip install -r requirements.txt`.
4. Run the bot `python3 bot.py`. This may take some time.

## Technologies Used
* This project uses an sqlite3 database to store users and their language settings, third-party dependencies, and an API.

* Python Version: 3.12.3