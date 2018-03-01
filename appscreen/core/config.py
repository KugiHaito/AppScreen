"""AppConfig Documentation.

This is part that load the configures
"""
from kivy.lang import Builder


class AppConfig():
    """docstring for AppConfig."""

    # app name
    __appname__ = 'Application'

    # app theme path
    __theme__ = ''

    # path icon
    __pathicon__ = 'resources/icon/'

    # set name icon
    __icon__ = 'icon.png'

    # width size window
    __width__ = 1180

    # height size window
    __height__ = 620

    # size app window
    __size__ = 1180, 620

    # single load theme
    theme_loaded = False

    def config(
        self,
        app_name=__appname__,
        app_icon=__icon__,
        app_size=__size__,
        min_width=__width__,
        min_height=__height__
    ):
        """
        Cofigure your application.

            `app_name` set title and global name app
            `app_icon` set a icon, just enter the icon name
            `app_size` set size of Window
                ex.:(width, height), _by default (1180, 550)_
            `min_width` set minimum with of Window, _by default 1180_
            `min_height` set minimum height of Window _by default 550_
        """
        self.__appname__ = app_name
        self.__icon__ = self.__pathicon__+app_icon+'.png'
        self.__size__ = app_size
        self.__width__ = min_width
        self.__height__ = min_height

    def load_theme(self, theme=__theme__):
        """Load Configures."""
        self.__theme__ = theme
        if self.__theme__ != '':
            Builder.load_file(self.__theme__)

    def unload_theme(self, theme=__theme__):
        """Unload theme before loaded."""
        self.__theme__ = theme
        Builder.unload_file(self.__theme__)

    def load_basic_template(self, template, ctx):
        """Load a template."""
        self.template = template
        self.ctx = ctx
        return Builder.template(self.template, **self.ctx)
