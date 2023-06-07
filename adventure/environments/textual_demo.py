from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Pretty, SelectionList
from textual.widgets.selection_list import Selection
from adventure.game import GameLogic


class WelcomeApp(App[None]):
    CSS_PATH = "selection_list_selected.css"

    def __init__(self, health, stamina, inventory):
        super().__init__()
        self.game = GameLogic("knife")
        self.health = health
        self.stamina = stamina
        self.inventory = inventory

    def compose(self) -> ComposeResult:
        yield Header("During your travels in some environments, some situation happens!!")
        yield SelectionList[str](
            Selection("Decision 1", 0),
            Selection("Decision 2", 1),
            Selection("Decision 3", 2),
            Selection("HP: ❤️" * self.health, 3),  # Combined label and heart emojis
            Selection("SP: 🍖" * self.stamina, 4),
            # Selection("🍖" * self.stamina, 5),  # Stamina emojis
            Selection("ITEMS:", 6),
            *[Selection(item, i + 7) for i, item in enumerate(self.inventory)],
        )
        yield Footer()

    def on_mount(self) -> None:
        selection_list = self.query_one(SelectionList[str])
        selection_list.border_title = "During your travels in some environments, some situation happens!!"

    def on_key(self, event):
        if event.key_code == "q":
            self.app.close()


if __name__ == "__main__":
    game = GameLogic("knife")
    app = WelcomeApp(game.health, game.stamina, game.inventory)
    app.run()
