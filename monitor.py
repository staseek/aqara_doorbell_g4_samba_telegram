"""
This script monitors a directory and sends new files to the telegram chat.
"""
import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class EndWritingHandler(LoggingEventHandler):
    """
    Custom handler. It works only on Linux-based OSes
    """
    def on_closed(self, event):
        print('closed event!')


def main():
    """
    Main function starts folder monitoring
    :return:
    """
    path = os.environ['MONITORING_PATH']
    telegram_chat_id = os.environ[]
    telegram_
    event_handler = EndWritingHandler()
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
