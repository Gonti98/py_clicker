from textual.screen import Screen
from textual.containers import CenterMiddle, Center
from textual.widgets import Button, Label, Footer
from textual.reactive import reactive

from src.utils.temp_save_load import Temp

class GameScreen(Screen):
    points: reactive[int] = reactive(0)
    BINDINGS = [
        ("space", "press_space", "to get points"),
        ("escape", "press_escape", "to main menu"),
    ]

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game

    def compose(self):
        yield CenterMiddle(
            Label(id="counter"),
        )
        yield Center(
            Button("Press SPACE to get points!", id="space-button", variant="primary"),
        )
        yield Footer()

    def on_mount(self) -> None:
        if self.new_game:
            self.points = 0
        else:
            self.points = Temp.load()

    def watch_points(self, points: int):
        self.query_one("#counter", Label).update(f"Coins: {points}")

    def action_press_space(self) -> None:
        self.points += 1

    def action_press_escape(self) -> None:
        Temp.save(self.points)
        self.app.switch_screen("Menu")
