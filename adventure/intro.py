from game import *
from rich.console import Console
import random
from rich.prompt import Prompt
from rich.style import Style


def introduction():
    console = Console()
    game_logic = GameLogic()
    random_items = random.sample(game_logic.items, 2)
    # print(game_logic.items)
    # print(random_items)
    # print(game_logic.inventory)

    decision = Prompt.ask(f"""
[bold yellow]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |                                                                                    |
 |                                                                                    |
 | Welcome to Anradesha! I'm your pilot [#FF5F1F]Ishmael[/#FF5F1F]. We will be touching down in the vast |
 | jungle in just a minute. Before you leave, I have a few items you might be         |
 | interested in. But here's the catch, you can only bring one.                       |
 |                                                                                    |
 |                                                                                    |
 | Please choose either the [#1F51FF]{random_items[0]}[/#1F51FF] or [#9D00FF]{random_items[1]}[/#9D00FF] to bring with you, 
 | they could be the difference between life and death out there, choose wisely...    |
 |                                                                                    |
  \                                                                                  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Choice""")
    while decision:
        if decision == random_items[0]:
            game_logic.inventory.append(random_items[0])
            console.print("""
[bold yellow]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                                                    |
| Good choice. Here we are, from now on, your on your own. Continue into the jungle  |
| to start your adventure. Good luck! [#FF5F1F]Ishmael[/#FF5F1F] out!                                   |
 \                                                                                   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """)
            break

        elif decision == random_items[1]:
            game_logic.inventory.append(random_items[1])
            console.print("""
[bold yellow]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                                                    |
| Good choice. Here we are, from now on, your on your own. Continue into the jungle  |
| to start your adventure. Good luck! [#FF5F1F]Ishmael[/#FF5F1F] out!                                   |
 \                                                                                   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
            break

        else:
            console.print("[bold yellow]Not a valid choice.")
            decision = Prompt.ask(f"""
[bold yellow]Please choose either the [#1F51FF]{random_items[0]}[/#1F51FF] or [#9D00FF]{random_items[1]}[/#9D00FF]
Choice""")


if __name__ == "__main__":
    introduction()
