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

import re
import glob
import tinycss2
from gi.repository import GLib, Gio
import os

import gettext
APP_NAME = "IBus-Theme"
LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")
gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

EXTENSION_URL = "https://extensions.gnome.org/extension/4112/customize-ibus/"
SOURCE_CODE_URL = "https://github.com/openSUSE/IBus-Theme-Tools"

# Output Style
BLACK_CYAN = "\033[1;30;46m"
READ_YELLOW = "\033[1;31;43m"
YELLOW_BLUE = "\033[1;33;44m"
UNDER_LINE = "\033[4m"
OUTPUT_END = "\033[0m"

gtkResource = ""


def getThemePathList():
    pathList = []
    pathList.append(os.path.join(GLib.get_home_dir(), ".themes"))
    pathList.append(os.path.join(GLib.get_user_data_dir(), "themes"))
    pathList.extend(list(map(lambda x: os.path.join(
        x, "themes"), GLib.get_system_data_dirs())))
    return pathList

# For Non-GNOME Desktop


def getAvailableGTKTheme():
    themeNameList = []
    themeNameLocation = {}
    GtkThemePath = []
    pathList = getThemePathList()
    for path in pathList:
        GtkThemePath.extend(glob.glob(path + "/*/*/gtk*.css"))
    for path in GtkThemePath:
        filename = os.path.basename(path)
        appendix = ""
        if "gtk-" in filename:
            appendix = ":" + filename.replace("gtk-", "").replace(".css", "")
        themeName = os.path.basename(
            os.path.dirname(os.path.dirname(path))) + appendix
        themeNameList.append(themeName)
        if themeName in themeNameLocation:
            themeNameLocation[themeName].append(path)
        else:
            themeNameLocation[themeName] = [path]
    return themeNameList, themeNameLocation


# def addStartup(themeName):
#     startupDir = os.path.join(GLib.get_user_config_dir(), "autostart")
#     if not os.path.exists(startupDir):
#         os.makedirs(startupDir)
#     with open(os.path.join(startupDir, "org.hollowman.ibus-gtk-theme-customize.desktop"), "w") as f:
#         content = "[Desktop Entry]\n" + \
#             "Name=ibus-gtk-theme-customize\n" + \
#             "Name[zh_CN]=ibus-gtk-主题自定义\n" + \
#             "GenericName=Customize IBus Theme\n" + \
#             "GenericName[zh_CN]=自定义IBus 主题\n" + \
#             "Icon=ibus\n" + \
#             "Exec=bash -c 'ibus exit;GTK_THEME=" + themeName + " ibus-daemon -dx &'\n" + \
#             "Comment=Applying user selected GTK theme for IBus\n" + \
#             "Comment[zh_CN]=应用用户选择的IBus GTK主题\n" + \
#             "Terminal=false\n" + \
#             "Type=Application\n" + \
#             "Categories=System;Settings;IBus;\n" + \
#             "StartupNotify=false\n"
#         f.write(content)


def RMUnrelatedGTKStyleClass(string, widgetList):
    classList = string.split(",")
    newClassList = []
    for className in classList:
        if any([className.strip().startswith(widget) for widget in widgetList]):
            if "#" not in className and ">" not in className and " " not in className.strip():
                if className.strip().startswith('.background'):
                    newClassList.append(className.strip().replace(
                        '.background', "#IBusCandidate", 1))
                else:
                    newClassList.append("#IBusCandidate " + className.strip())
                    if className.strip().startswith("box"):
                        newClassList.append(className.strip().replace(
                            "box", "#IBusCandidate", 1))
    return ", ".join(newClassList)


def GTKCustomizeImage():
    while True:
        print("")
        image = input(
            YELLOW_BLUE + _("Please enter your image file location (empty to exit file selection): ") + OUTPUT_END)
        if image:
            if os.path.isfile(image):
                cssContent = _("\n/* Customized Background Image */\n") + \
                    "#IBusCandidate {\n  background: url('" + image + "');\n  "
                while True:
                    print("")
                    print(
                        BLACK_CYAN + _("Please select repeat mode for your image:") + OUTPUT_END)
                    print("[" + BLACK_CYAN + "1" + OUTPUT_END + "]\t" + UNDER_LINE +
                          _("No") + OUTPUT_END)
                    print("[" + BLACK_CYAN + "2" + OUTPUT_END + "]\t" + UNDER_LINE +
                          _("Yes") + OUTPUT_END)
                    modeSelection = input(
                        YELLOW_BLUE + _("(Empty to be 1): ") + OUTPUT_END)
                    if modeSelection.isdigit() and int(modeSelection) >= 1 and int(modeSelection) <= 2 or not modeSelection:
                        if not modeSelection or modeSelection == "1":
                            cssContent += "background-repeat: no-repeat;\n  "
                        elif modeSelection == "2":
                            cssContent += "background-repeat: repeat;\n  "
                        while True:
                            print("")
                            print(
                                BLACK_CYAN + _("Please select sizing mode for your image:") + OUTPUT_END)
                            print("[" + BLACK_CYAN + "1" + OUTPUT_END + "]\t" + UNDER_LINE +
                                  _("Zoom") + OUTPUT_END)
                            print("[" + BLACK_CYAN + "2" + OUTPUT_END + "]\t" + UNDER_LINE +
                                  _("Full") + OUTPUT_END)
                            print("[" + BLACK_CYAN + "3" + OUTPUT_END + "]\t" + UNDER_LINE +
                                  _("Centered") + OUTPUT_END)
                            modeSelection = input(
                                YELLOW_BLUE + _("(Empty to be 1): ") + OUTPUT_END)
                            if modeSelection.isdigit() and int(modeSelection) >= 1 and int(modeSelection) <= 3 or not modeSelection:
                                if not modeSelection or modeSelection == "1":
                                    cssContent += "background-size: cover;\n"
                                elif modeSelection == "2":
                                    cssContent += "background-size: contain;\n"
                                elif modeSelection == "3":
                                    cssContent += "background-size: cover;\n"
                                while True:
                                    print("")
                                    radiusSetting = input(
                                        YELLOW_BLUE + _("Please input the image border radius you want to set in px(Empty to not set): ") + OUTPUT_END)
                                    if radiusSetting.isnumeric() or not radiusSetting:
                                        if radiusSetting.isnumeric():
                                            cssContent += "  border-radius: " + radiusSetting + "px;\n}"
                                        else:
                                            cssContent += "}"
                                        return cssContent
                                    else:
                                        print(
                                            READ_YELLOW + _("Error: Please Enter a Number!") + OUTPUT_END + "\n")
                            else:
                                print(
                                    READ_YELLOW + _("Error: Wrong selection!") + OUTPUT_END + "\n")
                    else:
                        print(READ_YELLOW +
                              _("Error: Wrong selection!") + OUTPUT_END + "\n")
            else:
                print(READ_YELLOW + _("Error: File Not Exists!") + OUTPUT_END + "\n")
        else:
            return ""


def exportGTKTheme():
    themeNameList, themeNameLocation = getAvailableGTKTheme()
    themeNameList = list(set(themeNameList))
    themeNameList.sort()
    count = 1
    while True:
        print(BLACK_CYAN +
              _("Please select a GTK theme to extract for IBus:") + OUTPUT_END)
        for themeName in themeNameList:
            print("[" + BLACK_CYAN+str(count)+OUTPUT_END + "]\t" +
                  UNDER_LINE + themeName + OUTPUT_END)
            count += 1
        print("[" + BLACK_CYAN + "q" + OUTPUT_END + "]\t" +
              READ_YELLOW + _("Exit") + OUTPUT_END)
        selection = input(YELLOW_BLUE + _("(Empty to exit): ") + OUTPUT_END)
        if selection == "q" or not selection:
            print(_("Goodbye!"))
            exit(0)
        elif selection.isdigit() and int(selection) < count and int(selection) > 0:
            while True:
                IBusThemeName = themeNameList[int(selection)-1]
                print("\n" + BLACK_CYAN +
                      _("Please select a GTK theme for other styles:") + OUTPUT_END)
                selection = input(
                    YELLOW_BLUE + _("(Empty to exit): ") + OUTPUT_END)
                if selection == "q" or not selection:
                    print(_("Goodbye!"))
                    exit(0)
                elif selection.isdigit() and int(selection) < count and int(selection) > 0:
                    mainThemeName = themeNameList[int(selection)-1]
                    cssContent = exportIBusGTKThemeCSS(
                        themeNameLocation[IBusThemeName][-1], themeNameLocation[mainThemeName][-1])
                    while True:
                        print("")
                        print(
                            BLACK_CYAN + _("Do you need a customized background image for IBus panel?") + OUTPUT_END)
                        print("[" + BLACK_CYAN + "1" + OUTPUT_END + "]\t" + UNDER_LINE +
                              _("No") + OUTPUT_END)
                        print("[" + BLACK_CYAN + "2" + OUTPUT_END + "]\t" + UNDER_LINE +
                              _("Yes") + OUTPUT_END)
                        modeSelection = input(
                            YELLOW_BLUE + _("(Empty to be 1): ") + OUTPUT_END)
                        if modeSelection.isdigit() and int(modeSelection) >= 1 and int(modeSelection) <= 2 or not modeSelection:
                            if not modeSelection or modeSelection == "1":
                                pass
                            elif modeSelection == "2":
                                cssContent += GTKCustomizeImage()
                            themeName = mainThemeName.replace(
                                ":", "-") + "-IBus-" + IBusThemeName.replace(":", "-")
                            path = os.path.join(
                                GLib.get_home_dir(), ".themes", themeName, "gtk-3.0")
                            if not os.path.exists(path):
                                os.makedirs(path)
                            with open(os.path.join(path, "gtk.css"), "w") as f:
                                f.write(cssContent)
                            if gtkResource:
                                with open(gtkResource, "rb") as s:
                                    with open(os.path.join(path, "gtk.gresource"), "wb") as d:
                                        d.write(s.read())
                            # os.system("ibus exit")
                            # os.system("GTK_THEME=" +
                            #         themeName + " ibus-daemon -dx &")
                            # addStartup(themeName)
                            print(YELLOW_BLUE +
                                  _("\nNow you can select: ") + themeName)
                            print(
                                _("in your desktop GTK theme settings to use the configuration above.") + OUTPUT_END)
                            print(_("Done! Goodbye!"))
                            exit(0)
                        else:
                            print(
                                READ_YELLOW + _("Error: Wrong selection!") + OUTPUT_END + "\n")
                else:
                    print(READ_YELLOW + _("Error: Wrong selection!") +
                          OUTPUT_END + "\n")
                    count = 1
        else:
            print(READ_YELLOW + _("Error: Wrong selection!") + OUTPUT_END + "\n")
            count = 1


def exportIBusGTKThemeCSS(styleSheet, mainStyleSheet, styleSheetContent=None, resource=True, recursive=False):
    newCSS = _("/*\n Generated by IBus Theme Tools\n") + \
        _(" Tool Author:") + " Hollow Man <hollowman@hollowman.ml>\n" + \
        _(" Tool Source Code:") + " " + SOURCE_CODE_URL + "\n" + \
        _(" Tool Licence:") + " GPLv3\n" + \
        _(" CSS Source File: ") + styleSheet + "\n" + \
        "*/\n\n" + \
        '@import url("' + mainStyleSheet + '");\n\n'
    if recursive:
        newCSS = _("/*\n Imported from CSS Source File: ") + \
            styleSheet + "\n*/\n\n"

    widgetList = ['*', 'box', 'label', 'button', '.background', 'separator']

    fileContent = ""
    if resource:
        with open(styleSheet) as f:
            fileContent = f.read()
    else:
        fileContent = styleSheetContent
    tokenList = tinycss2.parse_stylesheet(
        fileContent, skip_comments=True, skip_whitespace=True)
    otherDefinitionList = []
    for token in tokenList:
        if token.type == "qualified-rule":
            classStr = tinycss2.serialize(token.prelude)
            # For IBus candidate page button
            if any([widget in classStr for widget in widgetList]):
                classStr = RMUnrelatedGTKStyleClass(classStr, widgetList)
                if classStr:
                    contentStr = tinycss2.serialize(token.content)
                    contentStr = contentStr.replace(
                        "assets/", os.path.split(styleSheet)[0] + "/assets/")
                    newCSS += classStr + " {" + contentStr + "}\n\n"
        elif token.type == 'at-rule':
            if token.lower_at_keyword == 'import':
                for importToken in token.prelude:
                    if importToken.type == "function" and importToken.name == "url":
                        url = tinycss2.serialize(
                            importToken.arguments).strip("'").strip('"')
                        oldurl = url
                        url = os.path.join(
                            os.path.split(styleSheet)[0], url)
                        if not os.path.isfile(url):
                            global gtkResource
                            gtkResource = os.path.join(
                                os.path.dirname(styleSheet), "gtk.gresource")
                            if os.path.isfile(gtkResource):
                                Gio.Resource.load(gtkResource)._register()
                                success, content, etag = Gio.File.new_for_uri(
                                    oldurl).load_contents(None)
                                if success:
                                    content = content.decode("utf-8")
                                    newCSS += exportIBusGTKThemeCSS(
                                        oldurl, mainStyleSheet, content, False, True) + _("\n/* EOF */\n")
                            continue
                        newCSS += exportIBusGTKThemeCSS(
                            url, mainStyleSheet, "", True, True) + _("\n/* EOF */\n")
                        break
            elif token.lower_at_keyword == 'define-color' or token.lower_at_keyword == 'keyframes':
                prelude = tinycss2.serialize(token.prelude)
                content = ';'
                if token.content:
                    content = ' {' + tinycss2.serialize(token.content) + '}'
                otherDefinitionList.append('@' + token.lower_at_keyword + ' ' + prelude.strip() + content + '\n')
    for otherDefinition in otherDefinitionList:
        if otherDefinition.split(' ')[1] in newCSS:
            newCSS += otherDefinition
    return newCSS

# For GNOME Desktop


def getAvailableGNOMETheme():
    themeList = []
    pathList = getThemePathList()
    for path in pathList:
        themeList.extend(glob.glob(path + "/*/gnome-shell/gnome-shell.css"))
    pathList = list(map(lambda x: os.path.join(
        x, "gnome-shell", "theme"), GLib.get_system_data_dirs()))
    for path in pathList:
        themeList.extend(glob.glob(path + "/*.css"))
    return themeList


def RMUnrelatedStyleClass(string):
    classList = string.split(",")
    newClassList = []
    for className in classList:
        if ".candidate-" in className:
            newClassList.append(className)
    return ",".join(newClassList)


def exportIBusGNOMEThemeCSS(styleSheet, recursive=False):
    newCSS = _("/*\n Generated by IBus Theme Tools\n") + \
        _(" Tool Author:") + " Hollow Man <hollowman@hollowman.ml>\n" + \
        _(" Tool Source Code:") + " " + SOURCE_CODE_URL + "\n" + \
        _(" Tool Licence:") + " GPLv3\n" + \
        _(" CSS Source File: ") + styleSheet + "\n" + \
        _("\n Recommend to use Customize IBus GNOME Shell Extension:") + "\n " + EXTENSION_URL + "\n" + \
        _(" to change IBus theme by selecting this file.\n") + \
        "\n " + _("If you make any changes to this content after applying this file in above extension,\n") + \
        " " + _("for Customize IBus Extension before v68, please disable and then enable 'custom IME theme'\n") + \
        _(" again to make the changes take effect.\n") + \
        "\n " + _("Starting from v69, support stylesheets hot reload, CSS changes reflecting in real-time.") + \
        "\n*/\n\n"
    if recursive:
        newCSS = _("/*\n Imported from CSS Source File: ") + \
            styleSheet + "\n*/\n\n"
    # For fix candidate color
    globalColor = ""
    boxContent = ""
    popupContent = ""

    # For fix black border at pointer when system theme is black
    popupBoxpointerContent = ""

    # For unify system page button and IBus style page button
    pageButtonContent = ""

    with open(styleSheet) as f:
        tokenList = tinycss2.parse_stylesheet(
            f.read(), skip_comments=True, skip_whitespace=True)
        for token in tokenList:
            if token.type == "qualified-rule":
                classStr = tinycss2.serialize(token.prelude)
                cleanClassList = list(
                    map(lambda x: x.strip(), classStr.split(",")))
                # For IBus candidate page button
                if ".button" in classStr:
                    newCleanClassList = []
                    for cleanClass in cleanClassList:
                        if cleanClass == ".button":
                            # For IBus button radius fix
                            pageButtonContent += re.sub(r"\n(.+?)border-radius:(.+?);", "", tinycss2.serialize(
                                token.content))
                        elif cleanClass.startswith(".button"):
                            newCleanClassList.append(cleanClass.replace(
                                ".button", ".candidate-page-button"))
                        else:
                            newCleanClassList.append(cleanClass)
                    cleanClassList = newCleanClassList
                    classStr = ", ".join(cleanClassList) + " "

                # For get candidate color
                if ".popup-menu" in cleanClassList:
                    contentStr = tinycss2.serialize(token.content)
                    color = re.findall(r' color:(.+?);', contentStr)
                    if color:
                        globalColor = color[0]
                    else:
                        color = re.findall(r'\ncolor:(.+?);', contentStr)
                        if color:
                            globalColor = color[0]
                        else:
                            color = re.findall(r'\tcolor:(.+?);', contentStr)
                            if color:
                                globalColor = color[0]

                # For check if need to fix candidate color
                if ".candidate-box" in cleanClassList:
                    contentStr = tinycss2.serialize(token.content)
                    if not (" color:" in contentStr or "\ncolor:" in contentStr):
                        boxContent += contentStr
                        cleanClassList.remove(".candidate-box")
                        classStr = ", ".join(cleanClassList) + " "

                if ".candidate-popup-content" in cleanClassList:
                    contentStr = tinycss2.serialize(token.content)
                    popupContent += contentStr
                    cleanClassList.remove(".candidate-popup-content")
                    classStr = ", ".join(cleanClassList) + " "

                # For check if need to fix border at pointer
                if ".candidate-popup-boxpointer" in cleanClassList:
                    contentStr = tinycss2.serialize(token.content)
                    if not (" border-image:" in contentStr or "\nborder-image:" in contentStr):
                        popupBoxpointerContent += contentStr
                        cleanClassList.remove(".candidate-popup-boxpointer")
                        classStr = ", ".join(cleanClassList) + " "

                if ".candidate-page-button" in cleanClassList:
                    contentStr = tinycss2.serialize(token.content)
                    pageButtonContent += _("  /* IBus style page button */") + \
                        contentStr
                    cleanClassList.remove(".candidate-page-button")
                    classStr = ", ".join(cleanClassList) + " "

                if ".candidate-" not in classStr:
                    continue

                classStr = RMUnrelatedStyleClass(classStr)
                contentStr = tinycss2.serialize(token.content)
                contentStr = contentStr.replace(
                    "assets/", os.path.split(styleSheet)[0] + "/assets/")
                newCSS += classStr + "{" + contentStr + "}\n\n"
            elif token.type == 'at-rule' and token.lower_at_keyword == 'import':
                for importToken in token.prelude:
                    if importToken.type == "function" and importToken.name == "url":
                        url = tinycss2.serialize(
                            importToken.arguments).strip("'").strip('"')
                        if not os.path.isfile(url):
                            url = os.path.join(
                                os.path.split(styleSheet)[0], url)
                            if not os.path.isfile(url):
                                continue
                        newCSS += exportIBusGNOMEThemeCSS(
                            url, True) + _("\n/* EOF */\n")
                        break

    # Fix system IBus theme inherited in replaced theme
    if popupContent:
        if "background" not in popupContent:
            popupContent += _("  /* Fix system IBus theme background inherited in replaced theme */") + \
                "\n  background: transparent;\n"
        if "border" not in popupContent:
            popupContent += _("  /* Fix system IBus theme candidate window border inherited in replaced theme */") + \
                "\n  border: transparent;\n"
        if "box-shadow" not in popupContent:
            popupContent += _("  /* Fix system IBus theme candidate box shadow inherited in replaced theme */") + \
                "\n  box-shadow: none;\n"

    # Fix candidate color
    colorString = _("  /* Fix candidate color */") + \
        "\n  color:" + globalColor + ";\n"
    if not globalColor:
        colorString = ""
    if boxContent:
        newCSS += ".candidate-box {" + boxContent + colorString + "}\n\n"
    if " color:" in popupContent or "\ncolor:" in popupContent:
        colorString = ""
    if popupContent:
        newCSS += ".candidate-popup-content {" + \
            popupContent + colorString + "}\n\n"

    # Fix black border at pointer when system theme is black
    if popupBoxpointerContent:
        newCSS += ".candidate-popup-boxpointer {" + popupBoxpointerContent + _("  /* Fix black border at pointer when system theme is black */\n") + \
            "  border-image: none;\n}\n\n"

    # Unify system page button and IBus style page button
    if pageButtonContent:
        newCSS += _("/* Unify system page button and IBus style page button */\n")
        newCSS += ".candidate-page-button {" + pageButtonContent + "}\n"

    return newCSS


def exportIBusTheme():
    themeList = getAvailableGNOMETheme()
    themeList = list(set(themeList))
    themeList.sort()
    count = 1
    while True:
        print(BLACK_CYAN +
              _("Please select a GNOME theme to extract style sheet for IBus:") + OUTPUT_END)
        for theme in themeList:
            print("[" + BLACK_CYAN+str(count)+OUTPUT_END + "]\t" +
                  UNDER_LINE + theme.replace("/gnome-shell/gnome-shell.css", "") + OUTPUT_END)
            count += 1
        print("[" + BLACK_CYAN + "q" + OUTPUT_END + "]\t" +
              READ_YELLOW + _("Exit") + OUTPUT_END)
        selection = input(YELLOW_BLUE + _("(Empty to exit): ") + OUTPUT_END)
        if selection == "q" or not selection:
            print(_("Goodbye!"))
            exit(0)
        elif selection.isdigit() and int(selection) < count and int(selection) > 0:
            print("\n" +
                  BLACK_CYAN + _("Please enter the path to store generated stylesheet:") + OUTPUT_END)
            path = input(
                YELLOW_BLUE + _("(Empty to be 'exportedIBusTheme.css' in current directory): ") + OUTPUT_END)
            if not path:
                path = "exportedIBusTheme.css"
            newCSS = exportIBusGNOMEThemeCSS(themeList[int(selection)-1])
            with open(path, "w") as f:
                f.write(newCSS)
            print(YELLOW_BLUE +
                  _("\nNow you can use Customize IBus GNOME Shell Extension:\n") + EXTENSION_URL)
            print(
                _("to change IBus theme by selecting the extracted stylesheet.") + OUTPUT_END)
            print(YELLOW_BLUE + "\n" +
                  _("If you make any changes to this content after applying this file in above extension,\n") +
                  _("for Customize IBus Extension before v68, please disable and then enable 'custom IME theme'\n") +
                  _(" again to make the changes take effect.\n") + "\n" +
                  _("Starting from v69, support stylesheets hot reload, CSS changes reflecting in real-time.") +
                  OUTPUT_END)
            print(_("\nDone! Goodbye!"))
            exit(0)
        else:
            print(READ_YELLOW + _("Error: Wrong selection!") + OUTPUT_END + "\n")
            count = 1


def main():
    try:
        desktopEnv = os.environ["XDG_CURRENT_DESKTOP"].split(":")
    except Exception:
        print(READ_YELLOW + _("Error: Not in Linux!") + OUTPUT_END)
        exit(1)
    if "GNOME" in desktopEnv:
        exportIBusTheme()
    else:
        while True:
            print(BLACK_CYAN + _("Please select a mode:") + OUTPUT_END)
            print("[" + BLACK_CYAN + "1" + OUTPUT_END + "]\t" + UNDER_LINE +
                  _("Extract an IBus-related GTK theme") + OUTPUT_END)
            print("[" + BLACK_CYAN + "2" + OUTPUT_END + "]\t" + UNDER_LINE +
                  _("Extract an IBus-related GNOME theme stylesheet") + OUTPUT_END)
            print("[" + BLACK_CYAN + "q" + OUTPUT_END + "]\t" +
                  READ_YELLOW + _("Exit") + OUTPUT_END)
            modeSelection = input(
                YELLOW_BLUE + _("(Empty to be 1): ") + OUTPUT_END)
            if modeSelection == "q":
                print(_("Goodbye!"))
                exit(0)
            elif modeSelection.isdigit() and int(modeSelection) >= 1 and int(modeSelection) <= 2 or not modeSelection:
                if not modeSelection or modeSelection == "1":
                    print("")
                    exportGTKTheme()
                elif modeSelection == "2":
                    print(
                        "\n" + YELLOW_BLUE + _("Note: You can only apply the stylesheet under GNOME.") + OUTPUT_END + "\n")
                    exportIBusTheme()
            else:
                print(READ_YELLOW +
                      _("Error: Wrong selection!") + OUTPUT_END + "\n")


if __name__ == "__main__":
    main()
