import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
RFATRACK_SPREADSHEET_ENDPOINT = os.getenv("RFATRACK_SPREADSHEET_ENDPOINT")
RFATRACK_PROGRESS_FILE_PATH = os.getenv("RFATRACK_PROGRESS_FILE_PATH")
RFATRACK_ACCOUNT_SCREEN_NAME = os.getenv("RFATRACK_ACCOUNT_SCREEN_NAME")
