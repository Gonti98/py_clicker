from textual.screen import Screen
from textual.widgets import Footer

from src.config.bindings import BINDINGS

class SettingsMenu(Screen):
    BINDINGS = BINDINGS["SettingsMenu"]

    def compose(self):
        yield Footer()

    def action_press_escape(self) -> None:
        self.app.switch_screen("Menu")
