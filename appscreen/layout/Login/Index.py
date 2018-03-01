"""Sheet Documentation.

This is `Index` sheet
"""
from appscreen.sheets import BaseSheet
from kivy.uix.screenmanager import Screen


class Index(BaseSheet, Screen):
    """docstring for Index."""

    def __init__(self, name):
        """Init Index Sheet."""
        super(Index, self).__init__()
        self.name = name
        self.index(self.name)
