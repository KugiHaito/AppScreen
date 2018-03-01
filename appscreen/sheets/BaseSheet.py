"""Sheet Documentation.

This class assists the screens, to obtain similar values
"""
from appscreen.core.config import AppConfig


class BaseSheet(AppConfig):
    """docstring for BaseSheet."""

    __background__ = 'resources/Background/wallpaper_montains.jpg'

    __pathicon__ = 'resources/icon/'

    def index(self, name):
        """Init Index BaseSheet."""
        super(BaseSheet, self).__init__()
        self.name = name
        self.__sheet__ = self.name

    def go(self, page):
        """Go to page."""
        self.__page__ = page
        self.manager.current = self.__page__

    def get_appname(self):
        """Get sheets title."""
        return self.__appname__.swapcase().swapcase()

    def get_name(self):
        """Get title sheet."""
        return self.name.replace('_', ' ')

    def get_background(self):
        """Backgroun Image."""
        return self.__background__

    def get_icon(self, icon):
        """
        Load Icon.

        the image must have PNG extension
        """
        return self.__pathicon__+icon+'.png'
