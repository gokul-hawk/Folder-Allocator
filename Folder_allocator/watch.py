from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
from agent import move_file
BASE_DIR = os.path.expanduser("~/Downloads")
DEST_DIR = os.path.expanduser("~/Organized")
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            move_file(event.src_path)

observer = Observer()
observer.schedule(FileHandler(), BASE_DIR, recursive=False)
observer.start()

print(f"Watching: {BASE_DIR}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
