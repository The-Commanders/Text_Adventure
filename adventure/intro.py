from game import *
from rich.console import Console
import random
from rich.prompt import Prompt
from rich.style import Style


def introduction():
    console = Console()
    danger_style = Style(color="red", blink=True, bold=True)
    name = Prompt.ask("""
    [bold yellow]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |                                                                                    |
     |                                                                                    |
     |                                   Hello Adventurer!                                |
     |                                                                                    |
     |                      Before we get started, please input your name                 |
     |                 For best experience, increase the size of your terminal            |
     |                                                                                    |
      \                                                                                  /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     name""", default="Adventurer")

    tutorial = Prompt.ask(f"""
    [bold yellow]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |                                                                                    |
     |                                                                                    |
     |                              Good to meet you {name}!                              
     |                      We have a very important mission for you...                   |
     |                                                                                    |
     | Deep in the jungles of Anradesha, a long forgotten treasure is said to lye in      |
     | wait, the idol of power! This idol is said to grant the user with youth, riches,   |                                                                                
     | and knowledge beyond all belief! Your mission is to traverse through the dangerous |
     | region of Anradesha and return with the idol. There will be many obstacles along   |                                                                              
     | the way, as this will not be an easy journey. You will need to manage your...      |                                                                           
     |                                                                                    |
     | [i #FF3131]Health[/i #FF3131], if your health hits 0, its game over.                                      |
     | [i #FFFF33]Stamina[/i #FFFF33], if your stamina hits 0, you wont be able to succeed on decisions as much. |
     | [i #39FF14]Inventory[/i #39FF14], this is where all your gear will be stored. You have 2 slots.           |
     |                                                                                    |
     |                                                                                    |
     | Proceed through the 6 stages, survive the experience, and make your choices        |
     | carefully. Every decision counts! Good luck {name}!                                
     |                                                                                    |
     |           Please type "[green]play[/green]" to continue, or type "[red]quit[/red]" to end the game.          |
      \                                                                                  /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """, default="play")
    while tutorial:
        if tutorial == "play":
            break
        elif tutorial == "quit":
            console.print("""
    [bold yellow]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |                                                                                    |
     |                                                                                    |
     |                               Thank you for playing!                               |
     |                                                                                    |
     |                           Check out this project github                            |
     |                                                                                    |
     |                  https://github.com/The-Commanders/Text_Avdeventure                |
     |                                                                                    |
      \                                                                                  /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
            return
        else:
            tutorial = Prompt.ask("[bold yellow]Please type [green]play[/green] or [red]quit[/red] to proceed")

    item_list = ["survival knife", "grappling hook", "rope", "med spray", "ration"]
    random_items = random.sample(item_list, 2)
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
 | Please choose either the [i #1F51FF]{random_items[0]}[/i #1F51FF] or [i #9D00FF]{random_items[1]}[/i #9D00FF] to bring with you, 
 | they could be the difference between life and death out there, choose wisely...    |
 |                                                                                    |
  \                                                                                  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Choice""")
    while decision:
        if decision == random_items[0]:
            game_logic = GameLogic(decision)
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
            game_logic = GameLogic(decision)
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

    return game_logic


if __name__ == "__main__":
    introduction()
