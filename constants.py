import os
from dotenv import load_dotenv

load_dotenv()


class Security:
    TOKEN: str = os.getenv("BOT_TOKEN")
    CHANNEL_ID: str = os.getenv("CHANNEL_ID")


class Social:
    TELEGRAM_URL: str = os.getenv("TELEGRAM_URL")


class Message:
    MESSAGE: str = os.getenv("MESSAGE_TEXT")


class Scheduler:
    """Add here desired schedule"""

    JOBS = [
        {"hour": 22, "minute": 49},
        {"hour": 22, "minute": 50},
        {"hour": 22, "minute": 44},
        {"hour": 22, "minute": 27},
        {"hour": 21, "minute": 28},
    ]
