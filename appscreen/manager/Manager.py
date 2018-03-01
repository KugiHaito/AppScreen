"""Manager Documentation.

This is part that manage app
"""
from kivy.uix.screenmanager import ScreenManager, FadeTransition


class Paper(ScreenManager):
    """docstring for Manager."""

    sheets = []
    transition = FadeTransition()

    def add(self, *screen):
        """Add Screen."""
        self.sheets += screen

    def load(self):
        """Load Papers."""
        for paper in self.sheets:
            self.add_widget(paper)
