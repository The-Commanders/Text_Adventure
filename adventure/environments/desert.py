from game import *
from rich.console import Console
from rich.prompt import Prompt
import random
import time


class Desert:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.inventory = []

    def event_one(self):
        console = Console()
        console.print("""
    [bold yellow]You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.""")
        console.print("""

    [yellow]As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.""")

        choice = Prompt.ask("""
        [yellow]What will you do?
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
    [yellow]Exhausted, you walk back to the path you were taking.
    This took {rand_stam_loss} stamina.
""")
                break
            elif choice == "2":
                rand_stam_loss = random.randint(1, 2)
                self.stamina -= rand_stam_loss
                console.print(f"""[yellow]
    You continue on, not sure whether to trust your vision or not.
    The heat is is starting to get to you, but you cant give up now!
    This took {rand_stam_loss} stamina.
""")
                break

            elif choice == "3":
                if "ration" in self.inventory:
                    self.inventory.remove("ration")
                    rand_stam_gain = random.randint(1, 5)
                    self.stamina += rand_stam_gain
                    console.print(f"""[yellow]
    You consumed a [i #9D00FF]ration[/i #9D00FF], and feel better than ever!
    You continue on through the desert with extra stamina!
    You gained {rand_stam_gain} stamina!
""")
                    break
                else:
                    choice = Prompt.ask("""
[yellow]
    You do not have a [i #9D00FF]ration[/i #9D00FF] in your inventory. Please type 1 or 2.
""")

            else:
                choice = Prompt.ask("Please type 1, 2, or 3")

    def event_two(self):
        console = Console()
        console.print("""[yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.""")
        console.print("""
[yellow]
    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?""")

        choice = Prompt.ask("""
        [yellow]What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires grappling hook[/i #9D00FF])
    Choose 1, 2, or 3
Choice""")

        while choice:
            if choice == "1":
                console.print("""
                    [yellow]You chose the safe route. As you inch out, the sand starts sinking again!
                    You must act fast! Type the words you see on the screen to dig out![/yellow]
                    [red]Warning: 10 seconds will -2 points of health[/red]
                    """)

                start_time = time.time()
                qte_strs = ["dig", "push", "dig"]
                qte_index = 0
                while qte_index < len(qte_strs):
                    qte = Prompt.ask(f"""
            [b red]{qte_strs[qte_index]}[/b red]""")
                    if qte == qte_strs[qte_index]:
                        qte_index += 1
                    else:
                        console.print("""
            [b red]Wrong input![/b red]""")

                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 10:
                        self.health -= 2
                        start_time + time.time()  # Reset the start time

                console.print(f"""
    [bold yellow]
    Your quick thinking got you out of the quicksand!
    It took you {round(elapsed_time)} seconds to get out,
    that was close, but you can now continue your journey.
""")

                break

            elif choice == "2":
                rand_health_loss = random.randint(2, 4)
                self.health -= rand_health_loss
                console.print(f"""
    [red]Looks like the heat has clouded your judgment as well[/red]
    [yellow]Brute force made the sand envelop you much quicker, resulting in
    you almost suffocating in the process! Better be more careful.
    Your health decreased by {rand_health_loss} points.[/yellow]
""")
                break

            elif choice == "3":

                if "grappling hook" in self.inventory:
                    console.print("""
[bold yellow]
    Great thinking! Using the grappling hook, you through it over the gap
    hitting a rock and latching on! This saves you from struggling.
    You continue on through the desert
""")
                    break

                else:
                    choice = Prompt.ask("""
[bold yellow]
    You dont have the [i #9D00FF]grappling hook[/i #9D00FF] in your inventory!
    please type 1 or 2.
""")
            else:
                choice = Prompt.ask("""[yellow]
    Please type 1, 2, or 3
""")

    def event_three(self):
        console = Console()
        console.print("""[yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.""")
        console.print("""
[yellow]
    The desert sky is blue and clear, not a cloud in sight. After taking a second
    to admire the atmosphere and setting, you realise you've completely lost your
    sense of direction! You start to panic but collect your thoughts. What can
    help you remember where you've been? Take a second to collect your thoughts""")

        choice = Prompt.ask("""
        [yellow]What will you do?
    1. Use the sky for direction
    2. Book it in one direction
    3. Try to remember your surroundings
    Choose 1, 2, or 3
Choice""")

        while choice:
            if choice == "1":
                choice_2 = Prompt.ask("""
[yellow]
    Ok, you were headed north towards the ruins. The current time is 2:48.
    Using the suns position should get you back on track. Using your shadow 
    as reference, which direction is the sun currently?
                        Type either '[blue]east[/blue]' or '[blue]west[/blue]'
    """)
                if choice_2 == "east":
                    rand_stam_loss = random.randint(2, 3)
                    self.stamina -= rand_stam_loss
                    console.print(f"""
[yellow]
    [red]Incorrect:[/red]
    The sun sets in the west
    You set off towards the south and realise you are going backwards!
    This costs you {rand_stam_loss} stamina for going the wrong way!
""")
                    break
                elif choice_2 == "west":
                    console.print(f"""
[yellow]
    [green]Correct:[/green]
    The sun sets in the west
    You regain your sense of direction and continue on towards the
    ruins, great thinking!
""")
                    break
                else:
                    choice = Prompt.ask("""[yellow]
    Please type either east or west.
""")
            elif choice == "2":
                rand_stam_loss = random.randint(2, 5)
                self.stamina -= rand_stam_loss
                console.print(f"""
[yellow]
    For some reason you decide to run around like a mad man, getting you
    no where, and now your even more lost! Looks like going on in one direction
    wasn't the best choice, tiring you out with -{rand_stam_loss} stamina. You'll get
    out eventually right?
""")
                break

            elif choice == "3":
                console.print("""
[yellow]
    You remember seeing a few objects that can help you remember your direction.
    Unscramble the words to remember the objects you have seen to find the right
    direction to go!
        "lamp erte" "krco" "midrapy" "copsionr"
""")
                qte_strs = ["palm tree", "rock", "pyramid", "scorpion"]
                qte_index = 0
                while qte_index < len(qte_strs):
                    qte = Prompt.ask(f"""
                            [b red]unscramble[/b red]""")
                    if qte == qte_strs[qte_index]:
                        qte_index += 1
                        console.print("""[green]
                            Correct""")
                    else:
                        console.print("""
                            [b red]Wrong input![/b red]""")
                console.print(f"""
[bold yellow]
    Great work! You remembered the objects!
    As you continue walking, You see the palm tree you passed in the distance,
    you must be going the right way! You continue your journey
    """)
                break
            else:
                choice = Prompt.ask("""[yellow]
    Please type 1, 2, or 3
""")

