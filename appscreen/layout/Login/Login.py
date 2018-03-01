"""Login Layout Documentation.

This is a layout template for use
"""
from appscreen.core import AppConfig
from appscreen.manager import Paper
from appscreen.sheets import Launcher, BaseSheet

from .Index import Index
from .SignIn import SignIn
from .SignUp import SignUp
from .Home import Home

from kivy.uix.screenmanager import Screen


class Login(BaseSheet, AppConfig, Screen):
    """Layout Login Application."""

    app_name = AppConfig.__appname__

    icon = AppConfig.__icon__

    app_size = (AppConfig.__width__, AppConfig.__height__)

    min_width = AppConfig.__width__

    min_height = AppConfig.__height__

    def __init__(
        self,
        name='login',
        app_name='Login App',
        app_icon='applogin',
        app_size=app_size,
        min_height=min_height,
        min_width=min_width
    ):
        """Init Login application."""
        super(Login, self).__init__()
        self.name = name
        # set config app
        AppConfig.config(
            AppConfig,
            app_name=app_name,
            app_icon=app_icon,
            min_width=min_width,
            min_height=min_height
        )
        # reset theme to blank
        self.unload_theme('resources/theme/login.kv')
        self.load_theme('resources/theme/login.kv')

        # compact sheets
        self.sheets = Paper()
        self.sheets.add(
            Index(name='index'),
            SignIn(name='sign_in'),
            SignUp(name='sign_up'),
            Home(name='home')
        )

        # load base sheet
        self.index(self.name)
        self.config()
        # logger
        print("[INFO   ] [APP         ] Login application started ({})".format(
            self.name
            ))

    def add(self, *sheet):
        """Add a sheet in your application."""
        for paper in sheet:
            self.sheets.add(paper)

    def get_sheets(self):
        """Get Screen Names."""
        print(self.sheets.screens)

    def run(self):
        """Run Login application."""
        self.sheets.load()
        Launcher(self.sheets).run()
