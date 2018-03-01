"""Home Screen.

This is principal screen of the application
"""
from appscreen.sheets import BaseSheet
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class Home(BaseSheet, Screen):
    """docstring for Home."""

    def on_enter(self):
        """On screen loaded."""
        Window.maximize()
