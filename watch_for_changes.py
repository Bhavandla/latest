#!/usr/local/bin/python

# Python script to observe the changes in a directory
# on different events such as create, delete, move, modify
# create a new zip file of entire directory on each event and removes the existing zip file

import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import logging
from watchdog.events import LoggingEventHandler
import os
import shutil
from shutil import make_archive

# PatternMatchingEventHandler is a class which inherits FileEventHandler(from .Net) and we can use those methods
# Basically the events are :create, modified, deleted, moved

# The below methods can be executed
# on_any_event : It can be executed on all the above stated events, if they are defined
# created : When a file/directory is created the method will execute
# moved : when a file/directory is moved
# deleted: when a file/directory is deleted
# modified: when a file/directory is modified

# Above method can have three parameter and the first parameter is event object as first parameter
"""
	event_type : modified | created | moved | deleted
	is_directory : True | False
	src_path : Path to observe the file (which file/folder should be monitored)

"""

class MyHandler(PatternMatchingEventHandler):
    # patterns can be "*.xml", "*.lxml", "*.py", "*pyc"
    patterns = ["*"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type

        if os.path.isfile("/Users/filename.zip") == True:
            os.remove("/Users/filename.zip")
            print ("existing file is removed ")
            shutil.make_archive("directory", "zip", "/Users/directory/")
            print ("delete existing zip file and created a new zip file")
        else:
            print ("There is no zip file at the moment")
            shutil.make_archive("directory","zip", "/Users/directory")
            print (" A new zip file is created now ")

    def on_any_event(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.', recursive = True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
