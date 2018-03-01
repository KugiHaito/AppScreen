"""Blank Documentation.

This a theme application blank (no content)
"""
from appscreen.sheets import Launcher
from appscreen.core import AppConfig
from appscreen.sheets import BaseSheet

from kivy.uix.screenmanager import Screen


class Blank(BaseSheet, AppConfig, Screen):
    """This a theme application blank (no content by default)."""

    app_name = AppConfig.__appname__

    icon = AppConfig.__icon__

    app_size = (AppConfig.__width__, AppConfig.__height__)

    min_width = AppConfig.__width__

    min_height = AppConfig.__height__

    def __init__(
        self,
        name='blank',
        app_name='Blank App',
        app_icon='blank',
        app_size=app_size,
        min_height=min_height,
        min_width=min_width
    ):
        """Init template."""
        super(Blank, self).__init__()
        self.name = name
        # set app config
        AppConfig.config(
            AppConfig,
            app_name=app_name,
            app_icon=app_icon,
            min_width=0,
            min_height=0
        )
        # reset theme to blank
        self.unload_theme('resources/theme/blank.kv')
        self.load_theme('resources/theme/blank.kv')
        # load base sheet
        self.index(self.name)
        # load app config (default)
        self.config()
        print("[INFO   ] [APP         ] Blank application started ({})".format(self.name))

    def run(self):
        """Run Blank appscreen."""
        Launcher(self).run()
