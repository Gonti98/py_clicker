from textual.screen import Screen
from textual.containers import Center, CenterMiddle
from textual.widgets import Button, Label

class MainMenu(Screen):
    def compose(self):
        yield Center(
            Label("PLACEHOLDER", id="logo"),
        )

        yield CenterMiddle(
            Button("Continue", id="continue"),
            Button("Start", id="start"),
            Button("Settings", id="settings"),
            Button("Quit", id="quit"),
            id="menu",
        )
