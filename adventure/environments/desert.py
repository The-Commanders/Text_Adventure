from adventure.game import *
from rich.console import Console
from rich.prompt import Prompt
import random


class Desert:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10

    # Environment Intro
    # print("You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.")

    def event_one(self):
        console = Console()
        console.print("""
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.""")
        console.print("""

    As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.""")

        choice = Prompt.ask("""
        What will you do?
    1. Refile your stamina at the Oasis
    2. Ignore it and save your energy for more walking, your here for the treasure
    3. Eat a ration ([i #9D00FF]consumes ration[/i #9D00FF])
    Choose 1, 2, or 3
    Choice""")

        while choice:
            if choice == "1":
                rand_stam_loss = random.randint(3, 5)
                self.stamina -= rand_stam_loss
                console.print(f"""
    [bold red]Not good, you fell for a mirage![/bold red]
    Exhausted, you walk back to the path you were taking.
    This took {rand_stam_loss} stamina.
""")
                break
            elif choice == "2":
                rand_stam_loss = random.randint(1, 2)
                self.stamina -= rand_stam_loss
                console.print(f"""
    You continue on, not sure whether to trust your vision or not.
    The heat is is starting to get to you, but you cant give up now!
    This took {rand_stam_loss} stamina.
""")
                break

            elif choice == "3":
                if "ration" in GameLogic().inventory:
                    GameLogic().inventory.pop("ration")
                    rand_stam_gain = random.randint(1, 5)
                    self.stamina += rand_stam_gain
                    console.print(f"""
    You consumed a ration, and feel better than ever!
    You continue on through the desert with extra stamina!
    You gained {rand_stam_gain} stamina!
""")
                    break
                else:
                    choice = Prompt.ask("You do not have a ration in your inventory. Please type 1 or 2.")

            else:
                choice = Prompt.ask("Please type 1, 2, or 3")

    def event_two(self):
        console = Console()
        console.print("""
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.""")
        console.print("""

    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?""")

        choice = Prompt.ask("""
        What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires Grappling hook[/i #9D00FF])
    Choose 1, 2, or 3
    Choice""")

        while choice:
            if choice == "1":
                Prompt.ask("""
    [bold yellow]
    
    """)
                break

            elif choice == "2":
                rand_health_loss = random.randint(3, 5)
                self.health -= rand_health_loss
                console.print(f"""
    [red]Looks like the heat has clouded your judgment as well[/red]
    Brute force made the sand envelop you much quicker, resulting in
    you almost suffocating in the process! Better be more careful.
    Your health decreased by {rand_health_loss} points.
""")
                break

            elif choice == "3":
                pass
