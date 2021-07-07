# IBus 主题

[![last-commit](https://img.shields.io/github/last-commit/openSUSE/IBus-Theme-Tools)](https://github.com/openSUSE/IBus-Theme-Tools/graphs/commit-activity)

[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/openSUSE/IBus-Theme-Tools.svg)](https://github.com/openSUSE/IBus-Theme-Tools/archive/main.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/context:python)

[English](README.md)

[Python库依赖](../../network/dependencies)

## 前置知识

非GNOME桌面环境下，IBus的显示效果是由当前GTK主题确定的。

`$HOME/.config/gtk-3.0/settings.ini`文件定义了当前的GTK3主题及字体字号。

该文件的部分内容示例如下：

```ini
[Settings]
gtk-theme-name=Materia-light
gtk-font-name=更纱黑体 SC 12
```

上述表述中，`gtk-theme-name`指定了当前GTK主题为`Materia-light`，`gtk-font-name`指定了当前的字体为`更纱黑体 SC`，字号为`12`。

可通过修改上述文件实现改变IBus字体和字号的目的。

至于IBus的配色方案，可以在IBus启动的时候指定其使用特定GTK主题，即可实现对IBus配色的自定义。

## 实现功能

### 非GNOME桌面

在非 GNOME Shell 桌面环境中，可以更改IBus GTK主题。

运行[`IBus-Theme.py`](IBus-Theme.py)脚本，按提示操作选择GTK主题即可。

更改GTK主题后，程序会自动将更改IBus GTK主题的启动项加入当前用户的`$HOME/.config/autostart/`目录下。

示例启动项文件：[org.hollowman.ibus-gtk-theme-customize.desktop](org.hollowman.ibus-gtk-theme-customize.desktop)

如果你安装了支持GNOME-Shell样式的主题，你还可以选择提取IBus样式，但是只能在GNOME桌面使用。

### GNOME桌面

从GNOME-Shell主题提取IBus样式，使用Python下CSS解析器[tinycss2](https://github.com/Kozea/tinycss2)实现功能，生成额外IBus样式表供用户修改测试使用。

当用户从主题列表中选中一个主题，本程序会首先读取该主题的定义 CSS 文件，从中提取出定义 IBus 皮肤的类样式(`.candidate-*`)以及其他的额外操作，然后将其写入样式表文件。

随后可以使用[自定义 IBus GNOME Shell 扩展](https://extensions.gnome.org/extension/4112/customize-ibus/)导入并应用主题。

*注意：* 如果你在以上扩展中应用了被提取出的样式表后对文件内容作出了改变，请关闭并重新开启`自定义主题`来使改变生效。

示例提取出的样式表文件：[exportedIBusTheme.css](exportedIBusTheme.css)

## 使用自定义的GTK主题

创建一个名为`ibus-custom-theme`的GTK3主题：

`mkdir -p $HOME/.themes/ibus-custom-theme/gtk-3.0`

`$EDITOR $HOME/.themes/ibus-custom-theme/gtk-3.0/gtk.css`

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

_该项目是[@HollowMan6](https://github.com/HollowMan6)参与[谷歌编程之夏 (GSoC) 2021](https://summerofcode.withgoogle.com/projects/#5505085183885312) 于[OpenSUSE](https://github.com/openSUSE/mentoring/issues/158)社区成果的一部分。_
