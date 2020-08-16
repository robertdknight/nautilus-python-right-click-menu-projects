#!/usr/bin/env python
# Copyright (c) 2017-2020  Robert Knight
# All rights reserved.

# This creates a menu item that says "Open File With"
# and then, the two programs are options to open the file with.  In this particular example
# the names of the program are 'code' for Visual Studio code  and 'gedit'.
# to use leafpad instead of code, replace the word code with 'leafpad' on line 12.

from gi.repository import Nautilus, GObject
from urllib import unquote

PROGRAM_NAME = 'code'
PROGRAM_NAME2 = 'gedit'
PROGRAM_NAME3 = 'mousepad'
PROGRAM_NAME4 = 'gnome-builder'
PROGRAM_NAME5 = 'kate'


class ExampleMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def launch_program1(self, menu, files):
        if len(files) == 0:
            return
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        argv = [PROGRAM_NAME] + file_name
        GObject.spawn_async(argv, flags=GObject.SPAWN_SEARCH_PATH)

    def launch_program2(self, menu, files):
        if len(files) == 0:
            return
        # Strip the URI format to plain file names
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        argv = [PROGRAM_NAME2] + file_name
        GObject.spawn_async(argv, flags=GObject.SPAWN_SEARCH_PATH)

    def launch_program3(self, menu, files):
        if len(files) == 0:
            return
        # Strip the URI format to plain file names
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        argv = [PROGRAM_NAME3] + file_name
        GObject.spawn_async(argv, flags=GObject.SPAWN_SEARCH_PATH)
    
    def launch_program4(self, menu, files):
        if len(files) == 0:
            return
        # Strip the URI format to plain file names
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        argv = [PROGRAM_NAME4] + file_name
        GObject.spawn_async(argv, flags=GObject.SPAWN_SEARCH_PATH)
        
    def launch_program5(self, menu, files):
        if len(files) == 0:
            return
        # Strip the URI format to plain file names
        file_name = [unquote(item.get_uri()[7:]) for item in files]
        argv = [PROGRAM_NAME5] + file_name
        GObject.spawn_async(argv, flags=GObject.SPAWN_SEARCH_PATH)

    def get_file_items(self, window, files):

        #  Appears as top level item         ---------------------
        top_menuitem = Nautilus.MenuItem(name='ExampleMenuProvider::Main',
                                         label='Open File With: ',
                                         tip='',
                                         icon='')

        #  Submenu items when a file is selected -----------------
        
        submenu = Nautilus.Menu()
        top_menuitem.set_submenu(submenu)

        sub_menuitem = Nautilus.MenuItem(name='ExampleMenuProvider::Code',
                                         label='VS Code',
                                         tip='',
                                         icon='')
        submenu.append_item(sub_menuitem)
        sub_menuitem.connect('activate', self.launch_program1, files)

        sub_menuitem2 = Nautilus.MenuItem(name='ExampleMenuProvider::GEdit',
                                         label='Gedit',
                                         tip='',
                                         icon='')
        submenu.append_item(sub_menuitem2)
        sub_menuitem2.connect('activate', self.launch_program2, files)

        sub_menuitem3 = Nautilus.MenuItem(name='ExampleMenuProvider::Mousepad',
                                         label='Mousepad',
                                         tip='',
                                         icon='')
        submenu.append_item(sub_menuitem3)
        sub_menuitem3.connect('activate', self.launch_program3, files)
        
        sub_menuitem4 = Nautilus.MenuItem(name='ExampleMenuProvider::Builder',
                                         label='Builder',
                                         tip='',
                                         icon='')
        submenu.append_item(sub_menuitem4)
        sub_menuitem4.connect('activate', self.launch_program4, files)

        sub_menuitem5 = Nautilus.MenuItem(name='ExampleMenuProvider::Kate',
                                         label='Kate',
                                         tip='',
                                         icon='')
        submenu.append_item(sub_menuitem5)
        sub_menuitem5.connect('activate', self.launch_program5, files)
        
        return top_menuitem,
