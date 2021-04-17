# IBus 主题

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

(English version is down below)

[Python库依赖](../../network/dependencies)

## 前置知识

非Gnome桌面环境下，IBus的显示效果是由当前Gtk主题确定的。

`$HOME/.config/gtk-3.0/settings.ini`文件定义了当前的Gtk3主题及字体字号。

该文件的部分内容示例如下：

```ini
[Settings]
gtk-theme-name=Materia-light
gtk-font-name=更纱黑体 SC 12
```

上述表述中，`gtk-theme-name`指定了当前Gtk主题为`Materia-light`，`gtk-font-name`指定了当前的字体为`更纱黑体 SC`，字号为`12`。

可通过修改上述文件实现改变IBus字体和字号的目的。

至于IBus的配色方案，可以在IBus启动的时候指定其使用特定Gtk主题，即可实现对IBus配色的自定义。

## 实现功能

### 非GNOME桌面

在非 GNOME Shell 桌面环境中更改IBus GTK主题。

运行[`IBus-Theme.py`](IBus-Theme.py)脚本，按提示操作选择GTK主题即可。

更改GTK主题后，程序会自动将更改IBus GTK主题的启动项加入当前用户的`$HOME/.config/autostart/`目录下。

示例启动项文件：[org.hollowman.ibus-gtk-theme-customize.desktop](org.hollowman.ibus-gtk-theme-customize.desktop)

### GNOME桌面

从GNOME-Shell主题提取IBus样式，使用Python下CSS解析器tinycss2实现功能，生成额外IBus样式表供用户修改测试使用。

随后可以使用[Customize IBus GNOME Shell扩展](https://extensions.gnome.org/extension/4112/customize-ibus/)导入并应用主题。

*注意：* 如果你在以上扩展中应用了被提取出的样式表后对文件内容作出了改变，请按下 `Alt + F2` 然后按下 `r` 或者重新登录来重新加载 GNOME-Shell 来使改变生效。

示例提取出的样式表文件：[exportedIBusTheme.css](exportedIBusTheme.css)

## 使用自定义的GTK主题

创建一个名为`ibus-custom-theme`的Gtk3主题：

`mkdir -p $HOME/.theme/ibus-custom-theme/gtk-3.0`

`$EDITOR $HOME/.theme/ibus-custom-theme/gtk-3.0/gtk.css`

文件内容示例：

```css
* {
  color: #0b141a; /* 字体颜色 */
  background-color: #ffffff; /* 背景颜色 */
  -gtk-secondary-caret-color: #d4d4d4; /* 高亮背景颜色 */
}
```

然后在程序中选择`ibus-custom-theme`主题即可。

## 说明

_该项目是谷歌编程之夏 (GSoC) 2021 于[OpenSUSE](https://github.com/openSUSE/mentoring/issues/158)社区成果的一部分。_

# IBus Theme

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

### GNOME desktop

To do in the future...

Extracting IBus style from GNOME Shell theme, implement it using CSS parser library tinycss2 in Python. Additional IBus style sheets are generated for users to modify and test.

Then use the [Customize IBus GNOME Shell extension](https://extensions.gnome.org/extension/4112/customize-ibus/) to import and apply themes.

*Note:* If you make any changes to the extracted stylesheet after applying the file in above extension, please press `Alt + F2` and then `r` or re-login to reload the GNOME-Shell to make the changes take effect.

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
