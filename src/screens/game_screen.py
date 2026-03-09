from textual.screen import Screen
from textual.widgets import Footer, Digits, Label
from textual.reactive import reactive

from src.utils.temp_save_load import Temp
from src.game.grinding import Grind

class GameScreen(Screen):
    points: reactive[int] = reactive(0)
    grind: Grind = Grind(0.5, 1)
    BINDINGS = [
        ("space", "press_space", "to get coins"),
        ("escape", "press_escape", "to main menu"),
        ("1", "press_1", "buy Farm"),
        ("2", "press_2", "-1000"),
    ]

    # coins validate >= 0
    def validate_points(self, points: int) -> int:
        return max(0, points)

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game

    def compose(self):
        yield Digits(id="counter")
        yield Footer()

    def on_mount(self) -> None:
        if self.new_game:
            self.points = 0
        else:
            self.points = Temp.load()

    def watch_points(self, points: str):
        self.query_one("#counter", Digits).update(f"{points}")

    def action_press_space(self):
        self.points = self.grind.grind(self.points)

    def action_press_escape(self) -> None:
        Temp.save(self.points)
        self.app.switch_screen("Menu")
