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
import os

import gettext
APP_NAME = "IBus-Theme"
LOCALE_DIR = os.path.abspath("locale")
gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
gettext.textdomain(APP_NAME)
_ = gettext.gettext


def getAvailableGTKTheme():
    themeNameList = []
    pathList = [
        os.path.join(os.environ["HOME"], ".themes"),
        "/usr/share/themes"
    ]
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
    startupDir = os.path.join(
        os.environ["HOME"], ".config", "autostart")
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
    count = 1
    while True:
        print(_("Select a theme to apply:"))
        for themeName in themeNameList:
            print("["+str(count)+"] "+themeName)
            count += 1
        print("[q] "+_("Exit"))
        selection = input()
        if selection == "q":
            print(_("Goodbye!"))
            exit(0)
        if selection.isdigit() and int(selection) < count and int(selection) > 0:
            os.system("pkill ibus-daemon")
            os.system("GTK_THEME=" +
                      themeNameList[int(selection)-1] + " ibus-daemon -dx &")
            addStartup(themeNameList[int(selection)-1])
            print(_("Goodbye!"))
            break
        else:
            print(_("Error: Wrong selection!\n"))
            count = 1


def exportIBusTheme():
    print(_("To do in the future..."))
    print(_("Currently you can directly use Customize IBus GNOME Shell Extension: https://extensions.gnome.org/extension/4112/customize-ibus/"))
    print(_("to change GNOME Shell theme."))


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
