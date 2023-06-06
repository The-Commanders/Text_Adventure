import random
# from consumables import *


class Ruins_Halls:
    def __init__(self, print, prompt):
        self.name = "Ruins Halls"
        self.stamina = 10
        self.health = 10
        self.inventory = []
        self.items = []
        self.print = print
        self.prompt = prompt

    def event_one(self):
        self.print("""[blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    """)
        self.print("""[blue]
    Your journey has led you into an old room that appears to hold an
    old artifact, perhaps used by the previous inhabitants? who knows
    what it could be used for.. 
        What do you do?"
    1. Inspect the artifact closely
    2. Leave the artifact alone
    3. Take the artifact with you.
    """)

        while True:
            choice = self.prompt("""[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    """)
            if choice == '1':
                self.stamina -= random.randint(1, 2)
                self.print("""[blue]
    You carefully inspect the artifact and find a hidden compartment. 
    Inside, you discover a valuable gem. Your [yellow]stamina[/yellow] decreases slightly.
    """)
                break
            elif choice == '2':
                self.print("""[blue]
    You decide to leave the artifact undisturbed and continue your journey.
    """)
                break
            elif choice == '3':
                self.stamina -= random.randint(2, 3)
                self.print("""[blue]
    You decide to take the artifact with you, but it's heavy and tires you out. 
    Your [yellow]stamina[/yellow] decreases.
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[blue]
    [red]Invalid[/red] choice. Please enter a number between 1 and 3.
    """)

    def event_two(self):
        self.print("""[blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    """)
        self.print("""[blue]
    As you are walking through the hallways, mesmerised by all the exotic paintings,
    your carelessness has caused you to step on a floor trap! Quick, what will you do??
    1. Try to disarm the trap
    2. Jump over the trap
    3. Go back the way you came
    """)

        while True:
            choice = self.prompt("""[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    """)
            if choice == '1':
                self.health -= random.randint(2, 3)
                self.print("""[blue]
    You attempt to disarm the trap but trigger it instead. 
    You get injured, and your [red]health[/red] decreases.
    """)
                break
            elif choice == '2':
                self.stamina -= random.randint(1, 2)
                self.print("""[blue]
    You muster all your agility and successfully jump over the trap. 
    Your [yellow]stamina[/yellow] decreases slightly.
    """)
                break
            elif choice == '3':
                self.stamina -= random.randint(1, 2)
                self.print("""[blue]
    You decide it's best to go back the way you came and avoid the trap altogether. 
    Your [yellow]stamina[/yellow] decreases slightly.
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[blue]
    [red]Invalid[/red] choice. Please enter a number between 1 and 3.
    """)

    def event_three(self):
        self.print("""[blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    """)
        self.print("""[blue]
    You discover an iron door blocking your path, with no easy way around. 
    Quite literally stuck between a rock and a hard place, 
        what do you do?
    1. Look for a key to unlock the door
    2. Attempt to pick the lock
    3. Find an alternative route.
    """)

        while True:
            choice = self.prompt("""[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    """)
            if choice == '1':
                self.stamina -= random.randint(1, 2)
                self.print("""[blue]
    You search the surroundings and find a key hidden nearby. 
    Your [yellow]stamina[/yellow] decreases slightly.
    """)
                # self.inventory.append(random.choice(self.items))
                break
            elif choice == '2':
                self.health -= random.randint(2, 3)
                self.print("""[blue]
    You try to pick the lock but accidentally break your lockpick. 
    In the process, you injure yourself, and your [red]health[/red] decreases.
    """)
                break
            elif choice == '3':
                self.stamina -= random.randint(1, 2)
                self.print("""[blue]
    You decide to find an alternative route and discover a hidden passage that 
    leads past the locked door. Your [yellow]stamina[/yellow] decreases slightly.
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""
    [red]Invalid[/red] choice. Please enter a number between 1 and 3.
    """)

    # def play_game(self):
    #     self.display_text("Welcome to the Adventure Game!", Fore.MAGENTA)
    #
    #     challenge_message = "You have entered the Ruin Halls Challenge! 🏰"
    #     message_length = len(challenge_message)
    #     border = "=" * (message_length + 4)
    #
    #     self.display_text(border, Fore.YELLOW)
    #     self.display_text(f"| {' ' * message_length} |", Fore.YELLOW)
    #     self.display_text(f"| {challenge_message} |", Fore.YELLOW)
    #     self.display_text(f"| {' ' * message_length} |", Fore.YELLOW)
    #     self.display_text(border, Fore.YELLOW)
    #
    #     events = [self.situation_event_one, self.danger_event_one, self.puzzle_event_one]
    #     random.shuffle(events)
    #
    #     for event in events[:1]:  # Play only one event
    #         event()
    #         self.display_text("\n")
    #
    #         if self.health <= 0 or self.stamina <= 0:
    #             self.display_text("Game Over! Your health or stamina has reached 0. You failed your quest.", Fore.RED)
    #             return
    #
    #     self.display_text("Your current health: " + str(self.health), Fore.blue)
    #     self.display_text("Your current stamina: " + str(self.stamina), Fore.blue)
    #     self.display_text("Your inventory: " + str(self.inventory), Fore.blue)
    #     self.display_text("")  # Empty line for spacing
    #     self.display_text("You have completed the Ruin Halls scenario. Well done, adventurer!", Fore.GREEN)

# ruin_halls = Ruins_Halls("Ruin Halls")
# ruin_halls.play_game()

# Add the following code to prompt the user for the next challenge or to exit
# next_challenge = self.prompt("Type 'next' for the next challenge or 'q' to exit: ")
# while next_challenge.lower() != 'q':
#     ruin_halls.play_game()
#     next_challenge = self.prompt("Type 'next' for the next challenge or 'q' to exit: ")

# Exit the game
# self.print(Fore.GREEN + "Thank you for playing the game!" + Style.RESET_ALL)


if __name__ == "__main__":
    from rich.console import Console
    from rich.prompt import Prompt

    console = Console()
    env = Ruins_Halls(console.print, Prompt.ask)
    env.event_one()

