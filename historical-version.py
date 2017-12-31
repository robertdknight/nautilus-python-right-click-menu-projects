#!/usr/bin/env python
# Copyright (c) 2017 Robert Knight
# All rights reserved.


from gi.repository import Nautilus, GObject
from urllib import unquote
import os
import datetime


class historical_version(GObject.GObject, Nautilus.MenuProvider):
    """This adds a context menu item to create a copy of the file
    with a timestamp in the file name for easy backups prior to editing"""

    def __init__(self):
        pass

    def historical_version_the_file(self, menu, files):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        # Do whatever you want to do with the files selected
        if len(files) == 0:
            return
        # Strip the URI format to plain file names
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        print file_name[0]
        command = 'cp ' + file_name[0] + ' ' + file_name[0] + '_' + timestamp
        print command
        os.system(command)


    def get_file_items(self, window, files):
        # Show the menu if there is at least one file selected
        if len(files) == 0:
            return

        # Check to see if the selected item is a file or directory.  If the
        # selected item is not a file, then return from the function
        for selected_file in files:
            if selected_file.is_directory() or selected_file.get_uri_scheme() \
                    != 'file':
                return

        item = Nautilus.MenuItem(name='HistoricalVersion::ID_1',
                                 label='Historical Version',
                                 tip='',
                                 icon='')
        item.connect('activate', self.historical_version_the_file, files)

        return item,
