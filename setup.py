from setuptools import setup

setup(name='ibus-theme-tools',
      version='3',
      description='Change the IBus GTK theme or extracting IBus style from GNOME Shell theme.',
      url='https://github.com/openSUSE/IBus-Theme-Tools',
      author='Hollow Man',
      author_email='hollowman@hollowman.ml',
      license='GPL-3.0-or-later',
      long_description=open('README.md').read(),
      install_requires=['tinycss2', "python-gettext"],
      packages=['ibus_theme_tools'],
      package_data={'ibus_theme_tools': ['locale/**/LC_MESSAGES/*.mo']},
      entry_points={'console_scripts': [
          'ibus-theme-tools=ibus_theme_tools.ibus_theme_tools:main']},
      )
