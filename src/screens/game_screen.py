from textual.screen import Screen
from textual.containers import CenterMiddle
from textual.widgets import Label, Footer
from textual.reactive import reactive


class GameScreen(Screen):
    points = reactive(0)
    BINDINGS = [
        ("space", "press_space", "to get points"),
        ("escape", "press_escape", "to main menu"),
    ]

    def compose(self):
        yield CenterMiddle(Label("Press SPACE (0)", id="counter"))
        yield Footer()

    def action_press_space(self) -> None:
        self.points += 1
        self.query_one("#counter", Label).update(f"Press SPACE ({self.points})")

    def action_press_escape(self) -> None:
        self.app.pop_screen()
