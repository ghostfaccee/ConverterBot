import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_TOKEN = os.getenv('EXCHANGE_KEY')