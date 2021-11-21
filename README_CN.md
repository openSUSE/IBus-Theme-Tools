# IBus 主题工具

[![last-commit](https://img.shields.io/github/last-commit/openSUSE/IBus-Theme-Tools)](https://github.com/openSUSE/IBus-Theme-Tools/graphs/commit-activity)
[![pipy](https://img.shields.io/pypi/v/ibus-theme-tools.svg)](https://pypi.org/project/ibus-theme-tools/)

[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/openSUSE/IBus-Theme-Tools.svg)](https://github.com/openSUSE/IBus-Theme-Tools/archive/main.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/openSUSE/IBus-Theme-Tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/openSUSE/IBus-Theme-Tools/context:python)

### 欢迎在 Weblate 中贡献你的翻译！

[![翻译状态](https://hosted.weblate.org/widgets/ibus-customize/-/287x66-grey.png)](https://hosted.weblate.org/engage/ibus-customize/)

[English](README.md)

[Python库依赖](../../network/dependencies)

## 前置知识

IBus 的前端是基于 GTK 的，而 GNOME 用它的 GJS 版本取代了这个前端，使其与 GNOME 更加统一。

因而，对于非GNOME桌面环境，IBus的显示效果是由当前GTK主题确定的。

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

## 安装

你可以直接使用pip安装：

```bash
pip install ibus-theme-tools
ibus-theme-tools
```

或者也可以手动安装：

```bash
git clone https://github.com/openSUSE/IBus-Theme-Tools.git
cd IBus-Theme-Tools && python3 setup.py install
ibus-theme-tools
```

如果你使用 Arch Linux, 也可使用 AUR 安装:

```bash
yay -S ibus-theme-tools
```

[![AUR](https://aur.archlinux.org/css/archnavbar/aurlogo.png)](https://aur.archlinux.org/packages/ibus-theme-tools/)

openSUSE 可以直接通过[ymp 文件](https://software.opensuse.org/ymp/home:hollowman/openSUSE_Factory/ibus-theme-tools.ymp)安装。

你可以通过 [OpenSUSE OBS](https://software.opensuse.org//download.html?project=home%3Ahollowman&package=ibus-theme-tools) 下载绝大部分 Linux 发行版对应的相关安装包后安装。

Ubuntu 可使用 [PPA](https://launchpad.net/~hollowman86/+archive/ubuntu/ibus-theme-tools) 安装:

```bash
sudo add-apt-repository ppa:hollowman86/ibus-theme-tools
sudo apt-get update
```

对于 Gentoo，运行以下命令安装:

```bash
git clone https://github.com/openSUSE/IBus-Theme-Tools.git
cd IBus-Theme-Tools && make emerge
```

对于 NixOS:

```bash
sudo nix-env -i ibus-theme-tools
```

对于 Guix:

```bash
curl -o /tmp/guix.scm https://raw.githubusercontent.com/openSUSE/IBus-Theme-Tools/main/guix.scm
guix package -f /tmp/guix.scm
```

## 实现功能

### 非GNOME桌面

在非 GNOME Shell 桌面环境中，生成新的IBus GTK主题，并支持选择背景图片与配置圆角半径。

运行[`ibus_theme_tools.py`](ibus_theme_tools/ibus_theme_tools.py)脚本，按提示操作即可。

在主题生成完成后，手动在系统设置中选择新生成的主题即可。

如果你安装了支持GNOME-Shell样式的主题，你还可以选择提取IBus样式，但是只能在GNOME桌面使用。

#### 自定义 IBus 色调（创建一个GTK主题）

创建一个名为`ibus-custom-theme`的GTK3主题，运行：

```bash
mkdir -p $HOME/.themes/ibus-custom-theme/gtk-3.0
$EDITOR $HOME/.themes/ibus-custom-theme/gtk-3.0/gtk.css
```

然后进行文件内容的编辑，文件内容示例：

```css
* {
  color: #0b141a; /* 字体颜色 */
  background-color: #ffffff; /* 背景颜色 */
  -gtk-secondary-caret-color: #d4d4d4; /* 高亮背景颜色 */
}
```

然后运行程序，选择刚刚创建的`ibus-custom-theme`主题即可。

### GNOME桌面

从GNOME-Shell主题提取IBus样式，使用Python下CSS解析器[tinycss2](https://github.com/Kozea/tinycss2)实现功能，生成额外IBus样式表供用户修改测试使用。

运行[`ibus_theme_tools.py`](ibus_theme_tools/ibus_theme_tools.py)脚本，按提示操作即可。

当用户从主题列表中选中一个主题，本程序会首先读取该主题的定义 CSS 文件，从中提取出定义 IBus 皮肤的类样式(`.candidate-*`)以及其他的额外操作，然后将其写入样式表文件。

随后可以使用[自定义 IBus GNOME Shell 扩展](https://extensions.gnome.org/extension/4112/customize-ibus/)导入并应用主题。

*注意：* ~~如你的 IBus 样式表在应用后作出了更改，请关闭并重新开启对应`自定义主题`来使其生效。~~ 从 v69 开始，支持样式表热重载, CSS 的变化会实时地体现出来。

示例提取出的样式表文件：[exportedIBusTheme.css](exportedIBusTheme.css)

## 说明

_该项目曾是[@HollowMan6](https://github.com/HollowMan6)参与[谷歌编程之夏 (GSoC) 2021](https://summerofcode.withgoogle.com/archive/2021/projects/6295506795364352/) 于[OpenSUSE](https://github.com/openSUSE/mentoring/issues/158)社区成果的一部分。_
