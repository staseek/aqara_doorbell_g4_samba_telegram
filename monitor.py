"""
This script monitors a directory and sends new files to the telegram chat.
"""
import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileClosedEvent
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.types import FSInputFile
import asyncio
from concurrent.futures import ProcessPoolExecutor

class EndWritingHandler(LoggingEventHandler):
    """
    Custom handler. It works only on Linux-based OSes
    """
    def __init__(self, tg_bot_token: str, tg_chat_id: str, loop):
        super().__init__()
        self.tg_bot_token = tg_bot_token
        self.tg_chat_id = tg_chat_id
        self.bot = Bot(self.tg_bot_token)
        self.loop = loop

    async def bbb(self, event):
        try:
            await self.bot.send_message(chat_id=self.tg_chat_id,
                                        text="Появилось новая запись движения присылаю.")
            await self.bot.send_video(chat_id=self.tg_chat_id,
                                video=FSInputFile(event.src_path))
        except Exception as e:
            print(e)

    def on_closed(self, event: FileClosedEvent):
        print(event.is_directory, event.src_path)
        if not event.is_directory:
            self.loop.run_until_complete(self.bbb(event))


def main():
    """
    Main function starts folder monitoring
    :return:
    """
    load_dotenv()
    path = os.environ['MONITORING_FOLDER_VIDEO']
    telegram_chat_id = os.environ['TG_CHAT_ID']
    telegram_token = os.environ['TG_BOT_TOKEN']
    loop = asyncio.get_event_loop()
    p = ProcessPoolExecutor(2)  # Create a ProcessPool with 2 processes

    event_handler = EndWritingHandler(telegram_token, telegram_chat_id, loop)
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
