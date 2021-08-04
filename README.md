# IBus Theme Tools

[![last-commit](https://img.shields.io/github/last-commit/openSUSE/IBus-Theme-Tools)](https://github.com/openSUSE/IBus-Theme-Tools/graphs/commit-activity)
[![pipy](https://img.shields.io/pypi/v/ibus-theme-tools.svg)](https://pypi.org/project/ibus-theme-tools/)

[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/openSUSE/IBus-Theme-Tools.svg)](https://github.com/openSUSE/IBus-Theme-Tools/archive/main.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/context:python)

[中文 Chinese](https://github.com/openSUSE/IBus-Theme-Tools/blob/main/README_CN.md)

[Python Library Dependency](https://github.com/openSUSE/IBus-Theme-Tools/network/dependencies)

## Pre-knowledge

IBus has its front-end based on GTK, and GNOME replace that front-end with its GJS version to make it more unified with GNOME.

As a result, in non-GNOME Shell desktop environment, the display effect of IBus is determined by the current GTK theme.

`$HOME/.config/gtk-3.0/settings.ini` defines the current GTK3 theme and font size.

Example of the content of the file is as follows:

```ini
[Settings]
gtk-theme-name=Materia-light
gtk-font-name=更纱黑体 SC 12
```

In the above content, `gtk-theme-name` specifies that the current GTK theme is `material-light`, `gtk-font-name` specifies that the current font is `更纱黑体 SC` and the font size is `12 '.

The IBus font and font size can be changed by modifying the above documents.

As for the color scheme of IBus, you can specify that it uses specific GTK theme when IBus starts, and then customize the color matching of IBus.

## Installation

You can directly use pip to install:

```bash
pip install ibus-theme-tools
ibus-theme-tools
```

Or just install manually:

```bash
git clone https://github.com/openSUSE/IBus-Theme-Tools.git
cd IBus-Theme-Tools && python3 setup.py install
ibus-theme-tools
```

If you use Arch Linux, you can also use AUR to install as a system extension:

```bash
yay -S ibus-theme-tools
```

[![AUR](https://aur.archlinux.org/css/archnavbar/aurlogo.png)](https://aur.archlinux.org/packages/ibus-theme-tools/)

[Ubuntu PPA](https://launchpad.net/~hollowman86/+archive/ubuntu/ibus-theme-tools)

## Functionality

### Non-GNOME desktop

Change the IBus GTK theme in a non-GNOME Shell desktop environment and supporting to select a background picture or configure border radius.

Run [`ibus_theme_tools.py`](https://github.com/openSUSE/IBus-Theme-Tools/blob/main/ibus_theme_tools/ibus_theme_tools.py) script, operate according to prompted message.

After generating the new theme, just select the theme in the system theme configuration.

If you install themes that support GNOME shell style, you can also choose to extract IBus style, but you can only use it on GNOME desktop.

#### Customize IBus colors (Create a GTK theme)

Create a GTK3 theme called `ibus-custom-theme` by running:

```bash
mkdir -p $HOME/.themes/ibus-custom-theme/gtk-3.0
$EDITOR $HOME/.themes/ibus-custom-theme/gtk-3.0/gtk.css
```

then edit the file content. An example can be:

```css
* {
  color: #0b141a; /* Font Color */
  background-color: #ffffff; /* Background Color */
  -gtk-secondary-caret-color: #d4d4d4; /* Highlight Background Color */
}
```

After that, run the program, then select the theme `ibus-custom-theme` which you just created.

### GNOME desktop

Extracting IBus style from GNOME Shell theme, implement it using CSS parser library [tinycss2](https://github.com/Kozea/tinycss2) in Python. Additional IBus style sheets are generated for users to modify and test.

Run [`ibus_theme_tools.py`](https://github.com/openSUSE/IBus-Theme-Tools/blob/main/ibus_theme_tools/ibus_theme_tools.py) script, operate according to prompted message.

When user chooses a theme from the list, this script will first read the theme CSS file, extract the IBus related style classes (`.candidate-*`), then write it to stylesheet.

Then use the [Customize IBus GNOME Shell extension](https://extensions.gnome.org/extension/4112/customize-ibus/) to import and apply themes.

*Note:* If you make any changes to the extracted stylesheet after applying the file in above extension, please disable and then enable `custom IME theme` again to make the changes take effect.

Sample extracted stylesheet: [exportedIBusTheme.css](https://github.com/openSUSE/IBus-Theme-Tools/blob/main/exportedIBusTheme.css)

## Note

_This project is part of the achievement of [@HollowMan6](https://github.com/HollowMan6) partipating the [Google Summer of Code 2021](https://summerofcode.withgoogle.com/projects/#5505085183885312) at [OpenSUSE](https://github.com/openSUSE/mentoring/issues/158)._
