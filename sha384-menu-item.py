#!/usr/bin/env python
# Copyright (c) 2017 Robert Knight
# All rights reserved.


from gi.repository import Nautilus, GObject
import hashlib
import urllib


class Sha384MenuDisplay(GObject.GObject, Nautilus.MenuProvider):
    """ This places a SHA384 sum in the context menu in Nautilus.
    To use it, nautilus-python is required.  This script then goes in
    ~/.local/share/nautilus-python/extensions and should work after a restart
    of Nautilus
    """

    def __init__(self):
        pass

    def menu_activate_cb(self, menu, file):
        print "menu_activate_cb", file

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]
        filename = urllib.unquote(file.get_uri()[7:])
        sha384sum = hashlib.sha384()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), ''):
                sha384sum.update(chunk)
        f.close()
        string = sha384sum.hexdigest()
        item = Nautilus.MenuItem(name="Sha384MenuDisplay::Show_File_Name",
                                 label="SHA-384: %s" % string,
                                 tip="SHA-384: %s" % string)
        item.connect('activate', self.menu_activate_cb, file)

        return [item]

