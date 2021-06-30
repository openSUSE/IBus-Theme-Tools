# IBus Theme

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/IBus-Theme)](https://github.com/HollowMan6/IBus-Theme/graphs/commit-activity)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/IBus-Theme?style=social)](https://github.com/HollowMan6/IBus-Theme/watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/IBus-Theme?style=social)](https://github.com/HollowMan6/IBus-Theme/stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/IBus-Theme?style=social)](https://github.com/HollowMan6/IBus-Theme/network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/IBus-Theme.svg)](https://github.com/HollowMan6/IBus-Theme/archive/main.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/IBus-Theme.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/IBus-Theme/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/IBus-Theme.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/IBus-Theme/context:python)

[中文 Chinese](README_CN.md)

[Python Library Dependency](../../network/dependencies)

## Pre-knowledge

In non-GNOME Shell desktop environment, the display effect of IBus is determined by the current GTK theme.

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

## Implementation function

### Non-GNOME desktop

Change the IBus GTK theme in a non-GNOME Shell desktop environment.

Run [`IBus-Theme.py`](IBus-Theme.py) script, select GTK theme according to prompted message.

After changing the GTK theme, the program will automatically add the startup item of changing IBus GTK theme to the current user's `$HOME/.config/autostart/` directory.

Sample startup item file: [org.hollowman.ibus-gtk-theme-customize.desktop](org.hollowman.ibus-gtk-theme-customize.desktop)

If you install themes that support GNOME shell style, you can also choose to extract IBus style, but you can only use it on GNOME desktop.

### GNOME desktop

Extracting IBus style from GNOME Shell theme, implement it using CSS parser library [tinycss2](https://github.com/Kozea/tinycss2) in Python. Additional IBus style sheets are generated for users to modify and test.

When user chooses a theme from the list, this script will first read the theme CSS file, extract the IBus related style classes (`.candidate-*`), then write it to stylesheet.

Then use the [Customize IBus GNOME Shell extension](https://extensions.gnome.org/extension/4112/customize-ibus/) to import and apply themes.

*Note:* If you make any changes to the extracted stylesheet after applying the file in above extension, please disable and then enable `custom IME theme` again to make the changes take effect.

Sample extracted stylesheet: [exportedIBusTheme.css](exportedIBusTheme.css)

## Use custom GTK theme

Create a GTK3 theme called `ibus-custom-theme`:

`mkdir -p $HOME/.theme/ibus-custom-theme/gtk-3.0`

`$EDITOR $HOME/.theme/ibus-custom-theme/gtk-3.0/gtk.css`

Example of file content:

```css
* {
  color: #0b141a; /* Font Color */
  background-color: #ffffff; /* Background Color */
  -gtk-secondary-caret-color: #d4d4d4; /* Highlight Background Color */
}
```

Then select the IBus custom theme in the program.

## Note

_This project is part of the achievement of the Google Summer of Code 2021 at [OpenSUSE](https://github.com/openSUSE/mentoring/issues/158)._
