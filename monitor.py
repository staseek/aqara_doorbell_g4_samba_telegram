"""
This script monitors a directory and sends new files to the telegram chat.
"""
import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileClosedEvent
from dotenv import load_dotenv
from aiogram import Bot


class EndWritingHandler(LoggingEventHandler):
    """
    Custom handler. It works only on Linux-based OSes
    """
    def __init__(self, tg_bot_token: str, tg_chat_id: str):
        super().__init__()
        self.tg_bot_token = tg_bot_token
        self.tg_chat_id = tg_chat_id
        self.bot = Bot(self.tg_bot_token)

    def on_closed(self, event: FileClosedEvent):
        if not event.is_directory:
            self.bot.send_video(self.tg_chat_id, event.src_path)


def main():
    """
    Main function starts folder monitoring
    :return:
    """
    load_dotenv()
    path = os.environ['MONITORING_FOLDER_VIDEO']
    telegram_chat_id = os.environ['TG_CHAT_ID']
    telegram_token = os.environ['TG_BOT_TOKEN']
    event_handler = EndWritingHandler(telegram_token, telegram_chat_id)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
