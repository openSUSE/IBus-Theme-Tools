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
from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ibus-theme-tools',
      version='3.1.1',
      description='Change the IBus GTK theme or extracting IBus style from GNOME Shell theme.',
      url='https://github.com/openSUSE/IBus-Theme-Tools',
      author='Hollow Man',
      author_email='hollowman@hollowman.ml',
      license='GPL-3.0-or-later',
      install_requires=['tinycss2'],
      packages=['ibus_theme_tools'],
      package_data={'ibus_theme_tools': ['locale/**/LC_MESSAGES/*.mo']},
      entry_points={'console_scripts': [
          'ibus-theme-tools=ibus_theme_tools.ibus_theme_tools:main']},
      long_description=long_description,
      project_urls={
          "Bug Tracker": "https://github.com/openSUSE/IBus-Theme-Tools/issues",
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: Unix",
          "Topic :: Desktop Environment :: Gnome",
          "Natural Language :: Chinese (Simplified)",
          "Natural Language :: English"
      ],
      long_description_content_type='text/markdown'
      )
