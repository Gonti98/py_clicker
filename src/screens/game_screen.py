from textual.screen import Screen
from textual.containers import CenterMiddle, Center
from textual.widgets import Label


class GameScreen(Screen):
    def compose(self):
        yield CenterMiddle(Label("Press SPACE (0)", id="counter"))
