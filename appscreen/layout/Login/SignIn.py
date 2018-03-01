"""Sign In Screen.

This is principal screen of the application
"""
from appscreen.sheets import BaseSheet
from kivy.uix.screenmanager import Screen


class SignIn(BaseSheet, Screen):
    """docstring for SignIn."""

    def __init__(self, name):
        """Init Index Sheet."""
        super(SignIn, self).__init__()
        self.name = name
        self.index(self.name)

    def on_enter(self):
        """On screen loaded."""
        self.ids.get('nick').focus = True  # Focus in first TextInput
