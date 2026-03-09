from textual.screen import Screen
from textual.widgets import Footer, Digits, Label
from textual.reactive import reactive

from src.utils.temp_save_load import Temp
from src.game.grinding import Grind

class GameScreen(Screen):
    coins: reactive[int] = reactive(0)
    grind: Grind = Grind(0.5, 1)
    BINDINGS = [
        ("space", "press_space", "to get coins"),
        ("escape", "press_escape", "to main menu"),
        ("1", "press_1", "buy Farm"),
        ("2", "press_2", "-1000"),
    ]

    # coins validate >= 0
    def validate_coins(self, coins: int) -> int:
        return max(0, coins)

    def __init__(self, new_game: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.new_game = new_game

    def compose(self):
        yield Digits(id="counter")
        yield Footer()

    def on_mount(self) -> None:
        if self.new_game:
            self.coins = 0
        else:
            self.coins = Temp.load()

    def watch_coins(self, coins: str):
        self.query_one("#counter", Digits).update(f"{coins}")

    def action_press_space(self):
        self.coins = self.grind.grind(self.coins)

    def action_press_escape(self) -> None:
        Temp.save(self.coins)
        self.app.switch_screen("Menu")
