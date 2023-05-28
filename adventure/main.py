from game import *
from intro import introduction
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
## class imports
from environments.jungle import Jungle
from environments.river import River


def main():
    console = Console()
    # danger_style = Style(color="red", blink=True, bold=True)
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
            introduction()
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


    ## Anthony's testing code' start
    # game = GameLogic()
    # jungle = Jungle("jungle")
    # game.add_environment(jungle)
    # print(f"this is an instance of Jungle: {jungle}")
    # print(game)
    # str(game)
    # game.traverse_environments()
    ## Anthony's testing code end

    ## Deiosha's testing code
    game = GameLogic()
    river = River("river")
    game.add_environment(river)
    game.traverse_environments()






if __name__ == "__main__":
    main()
    #pass
