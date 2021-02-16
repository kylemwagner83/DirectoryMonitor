import time
import os
import configparser
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from updateJSON import update_games_json, update_movies_json, update_tvshows_json
from updateDB import update_games_db, update_movies_db, update_tvshows_db



mediapath = "Media"

if os.path.isfile("Data/settings.ini"):
    config = configparser.ConfigParser()
    config.read("Data/settings.ini")
    mediapath = config["Media Folder Path"]["mediapath"]

gamespath = mediapath + "/Games"
moviespath = mediapath + "/Movies"
tvshowspath = mediapath + "/TV Shows"


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def something_changed(event):
    if "\Games" in f"{event.src_path}":
        update_games_json(gamespath)
        update_games_db()

    if "\Movies" in f"{event.src_path}":
        update_movies_json(moviespath)
        update_movies_db()

    if "\TV Shows" in f"{event.src_path}":
        update_tvshows_json(tvshowspath)
        update_tvshows_db()


my_event_handler.on_created = something_changed
my_event_handler.on_deleted = something_changed
my_event_handler.on_moved = something_changed

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, mediapath, recursive=go_recursively)


my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
