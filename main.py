import telebot
import logging
import time
from constants import Security, Message, Scheduler
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

bot = telebot.TeleBot(Security.TOKEN)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

CHANNEL_ID = Security.CHANNEL_ID


class TelegramBot:
    """Telegram Bot class for API interaction and scheduling messages."""

    def __init__(self):
        """Initialize the bot and start the scheduler."""
        self.scheduler = BackgroundScheduler()
        self._schedule_messages()

    def _schedule_messages(self):
        """Schedule message sending based on defined cron jobs."""
        for job in Scheduler.JOBS:
            self.scheduler.add_job(
                self.send_message_reminder,
                "cron",
                hour=job["hour"],
                minute=job["minute"],
            )
        self.scheduler.start()

    @staticmethod
    def send_message_reminder():
        """Send a scheduled message to the channel."""
        try:
            bot.send_message(
                CHANNEL_ID,
                Message.MESSAGE,
                parse_mode="HTML",
            )
            log.info("Scheduled message sent successfully")
        except Exception as e:
            log.error(f"An error occurred during sending a message: {e}")

    @staticmethod
    def start_polling():
        """Start polling for incoming messages."""
        while True:
            try:
                bot.infinity_polling(timeout=10, long_polling_timeout=5)
            except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.error(
                    f"Error occurred during polling at {current_time}. Exception: {e}"
                )
                time.sleep(60)


if __name__ == "__main__":
    telegram_bot = TelegramBot()
    telegram_bot.start_polling()
