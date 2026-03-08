from textual.screen import Screen
from textual.containers import Center, CenterMiddle
from textual.widgets import Button, Label

from assets.logo import TITLE_ASCII
from src.screens.game_screen import GameScreen
from src.utils.temp_save_load import Temp

class MainMenu(Screen):
    def compose(self):
        yield Center(Label(TITLE_ASCII, id="logo"))
        yield CenterMiddle(
            Button("Continue", id="continue", disabled=True),
            Button("New Game", id="start_new_game"),
            Button("Settings", id="settings", disabled=True),
            id="menu",
        )

    def on_mount(self) -> None:
        has_save = Temp.TEMP_SAVE_FILE.exists()
        continue_btn = self.query_one("#continue", Button)
        continue_btn.disabled = not has_save

    def on_screen_resume(self) -> None:
        self.refresh()
        if Temp.TEMP_SAVE_FILE.exists():
            self.query_one("#continue", Button).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        match button_id:
            case "continue":
                self.app.switch_screen(GameScreen(new_game=False))
            case "start_new_game":
                self.app.switch_screen(GameScreen())
            case "settings":
                self.app.notify("Settings!")
            case _:
                self.app.notify(f"Error: {button_id}")
