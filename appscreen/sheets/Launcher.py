"""Launcher Documentation.

This is `Launcher` sheet
"""
from appscreen.core import AppConfig

from kivy.core.window import Window
from kivy.app import App


class Launcher(App, AppConfig):
    """docstring for Main."""

    def __init__(self, sheets):
        """Init Main."""
        super(Launcher, self).__init__()
        self.sheets = sheets

    def build(self):
        """Build appscreen."""
        self.title = self.__appname__
        self.icon = self.__icon__
        # window settings
        Window.size = self.__size__
        Window.minimum_width = self.__width__
        Window.minimum_height = self.__height__
        # window position
        Window.top = 80
        Window.left = 80
        # return sheets
        return self.sheets
