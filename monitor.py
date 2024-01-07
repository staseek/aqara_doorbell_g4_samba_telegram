import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class EndWritingHandler(LoggingEventHandler):
    def on_closed(self, event):
        print('closed event!')

def main():
    path = os.environ['MONITORING_PATH']
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
