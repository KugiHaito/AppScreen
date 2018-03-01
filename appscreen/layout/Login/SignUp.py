"""Sign Up Screen.

This is principal screen of the application
"""
from appscreen.sheets import BaseSheet
from kivy.uix.screenmanager import Screen


class SignUp(BaseSheet, Screen):
    """docstring for SignUp."""

    def __init__(self, name):
        """Init Index Sheet."""
        super(SignUp, self).__init__()
        self.name = name
        self.index(self.name)

    def on_enter(self):
        """On screen loaded."""
        self.ids.get('nick').focus = True  # Focus in first TextInput
