#!/usr/bin/python3
# vim: set fileencoding=utf-8 :
# vim: set et ts=4 sw=4:
'''
  IBus Theme Tools
  Author:  Hollow Man <hollowman@hollowman.ml>

  Copyright © 2021 Hollow Man(@HollowMan6). All rights reserved.

  This document is free software; you can redistribute it and/or modify it under the terms of the GNU General
  Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option)
  any later version.
'''
from gi.repository import GLib
import os

import gettext
APP_NAME = "IBus-Theme"
LOCALE_DIR = os.path.abspath("locale")
gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
gettext.textdomain(APP_NAME)
_ = gettext.gettext


def getThemePathList():
    pathList = []
    pathList.append(os.path.join(GLib.get_home_dir(), ".themes"))
    pathList.append(os.path.join(GLib.get_user_data_dir(), "themes"))
    pathList.extend(list(map(lambda x: os.path.join(
        x, "themes"), GLib.get_system_data_dirs())))
    return pathList


def getAvailableGTKTheme():
    themeNameList = []
    pathList = getThemePathList()
    GTKVersionList = ["3.0", "3.20", "4.0"]
    for path in pathList:
        if os.path.isdir(path):
            files = os.listdir(path)
            for p in files:
                if os.path.isdir(os.path.join(path, p)):
                    for version in GTKVersionList:
                        if os.path.isfile(os.path.join(path, p, "gtk-"+version, "gtk.css")):
                            themeNameList.append(p)
                            break
    return themeNameList


def addStartup(themeName):
    startupDir = os.path.join(GLib.get_user_config_dir(), "autostart")
    if not os.path.exists(startupDir):
        os.makedirs(startupDir)
    with open(os.path.join(startupDir, "org.hollowman.ibus-gtk-theme-customize.desktop"), "w") as f:
        content = "[Desktop Entry]\n" + \
            "Name=ibus-gtk-theme-customize\n" + \
            "Name[zh_CN]=ibus-gtk-主题自定义\n" + \
            "GenericName=Customize IBus Theme\n" + \
            "GenericName[zh_CN]=自定义IBus 主题\n" + \
            "Icon=ibus\n" + \
            "Exec=bash -c 'pkill ibus-daemon;GTK_THEME=" + themeName + " ibus-daemon -dx &'\n" + \
            "Comment=Applying user selected GTK theme for IBus\n" + \
            "Comment[zh_CN]=应用用户选择的IBus GTK主题\n" + \
            "Terminal=false\n" + \
            "Type=Application\n" + \
            "Categories=System;Settings;IBus;\n" + \
            "StartupNotify=false\n"
        f.write(content)


def changeGTKTheme():
    themeNameList = getAvailableGTKTheme()
    themeNameList.sort()
    count = 1
    while True:
        print(_("Please select a GTK theme to apply for IBus:"))
        for themeName in themeNameList:
            print("["+str(count)+"]\t"+themeName)
            count += 1
        print("[q]\t"+_("Exit"))
        selection = input(_("(Empty to exit): "))
        if selection == "q" or not selection:
            print(_("Goodbye!"))
            exit(0)
        elif selection.isdigit() and int(selection) < count and int(selection) > 0:
            while True:
                print(_("Please select a theme mode (Not guaranteed to work):"))
                print("[0]\t"+_("Default"))
                print("[1]\t"+_("Light"))
                print("[2]\t"+_("Dark"))
                print("[q]\t"+_("Exit"))
                modeSelection = input(_("(Empty to be default): "))
                if modeSelection == "q":
                    print(_("Goodbye!"))
                    exit(0)
                elif modeSelection.isdigit() and int(modeSelection) >= 0 and int(modeSelection) <= 2 or not modeSelection:
                    mode = ""
                    if not modeSelection or modeSelection == "0":
                        pass
                    elif modeSelection == "1":
                        mode = ":light"
                    elif modeSelection == "2":
                        mode = ":dark"
                    os.system("pkill ibus-daemon")
                    os.system("GTK_THEME=" +
                              themeNameList[int(selection)-1] + mode + " ibus-daemon -dx &")
                    addStartup(themeNameList[int(selection)-1] + mode)
                    print(_("Done! Goodbye!"))
                    exit(0)
                else:
                    print(_("Error: Wrong selection!\n"))
        else:
            print(_("Error: Wrong selection!\n"))
            count = 1


def exportIBusTheme():
    print(_("To do in the future..."))
    print(_("Currently you can directly use Customize IBus GNOME Shell Extension: https://extensions.gnome.org/extension/4112/customize-ibus/"))
    print(_("to change IBus theme by specifying GNOME Shell theme."))


if __name__ == "__main__":
    try:
        desktopEnv = os.environ["XDG_CURRENT_DESKTOP"].split(":")
    except Exception:
        print(_("Error: Not in Linux!"))
        exit(1)
    if "GNOME" in desktopEnv:
        exportIBusTheme()
    else:
        changeGTKTheme()
