from textual.app import App, ComposeResult


class MyGameApp(App):
    CSS_PATH = "../assets/style.tcss"


if __name__ == "__main__":
    app = MyGameApp()
    app.run()
