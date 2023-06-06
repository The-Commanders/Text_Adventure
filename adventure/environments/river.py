import random
from colorama import Fore, Style
from adventure.consumables import *



class River:
    def __init__(self, print, prompt):
        self.name = "River"
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = []
        self.print = print
        self.prompt = prompt

#     def display_text(self, text, color=None):
#         if color:
#             print(color + text + Fore.RESET)
#         else:
#             print(text)

#     def item_collection(self):
#         self.display_text("Items in the game:", Fore.CYAN)
#         for item in self.items:
#             self.display_text("- " + item, Fore.CYAN)

    def event_one(self):
        self.print("""[cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    """)
        self.print("""[cyan]
    The base of the river seems to have no simple way across, just your luck!
    How will you get across, looks like there are a few ways..
    1. Swim across the river
    2. Build a makeshift raft and sail across
    3. Look for a bridge upstream.
    """)

        while True:
            choice = self.prompt("""[cyan]
    Enter your choice (1-3), enter 'i' to use an item: 
    """)
            if choice == "1":
                random_stam_loss = random.randint(1, 3)
                self.stamina -= random_stam_loss
                self.print(f"""[cyan]
    You swim across the river. It was tiring, and you lost [yellow]]{random_stam_loss} stamina[/yellow].
    """)
                break
            elif choice == "2":
                # self.inventory.append("Raft")
                random_hp_loss = random.randint(2, 4)
                self.health -= random_hp_loss
                self.print(f"""[cyan]
    You build a makeshift raft and sail across the river. As you sail across, you remember that you have zero experience
    with building a raft. The raft sinks and you are forced to swim the rest of the way. You lost [red]{random_hp_loss} 
    health[/red] from entire ordeal!
    """)
                break
            elif choice == "3":
                self.print("""[cyan]
    You find a bridge upstream and cross the river [green]safely[/green].
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[cyan]
    [red]Invalid[/red] choice. Please enter a number between 1 and 3.
    """)

        # self.print("[white]Your current health: " + str(self.health))
        # self.print("[white]Your current stamina: " + str(self.stamina))
        # self.print("[white]Your inventory: " + str(self.inventory))

    #     if self.stamina <= 0:
    #         self.health -= random.randint(2, 4)
    #         self.print("""[cyan]
    # The swim drained your [yellow]stamina[/yellow], and you lost some [red]health[/red].
    # """)
    #     elif self.stamina >= 10:
    #         self.health += random.randint(1, 3)
    #         self.print("""[cyan]
    # You handled the swim well and gained some [red]health[/red].
    # """)

    def event_two(self):
        self.print("""[cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    """)
        self.print("""[cyan]
    As you traverse the riverside looking for a way across, you encounter a dangerous
    crocodile, and he looks hungry!
        What do you do?
    1. Fight the creature.
    2. Try to evade the danger.
    3. Stand your ground.
    """)

        while True:

            choice = self.prompt("""[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input""")
            if choice == "1":
                random_hp_lost = random.randint(4, 6)
                self.stamina -= random_hp_lost
                self.print(f"""[cyan]
    You take on the croc Happy Gilmore style. Except, this is anything at all like the movie! Instead you are badly 
    injured by the crocodile! You lost [red]{random_hp_lost} HP[/red].
    """)
                break
            elif choice == "2":
                random_stam_loss = random.randint(1, 3)
                self.stamina -= random_stam_loss
                self.print(f"""[cyan]
    You manage to evade the danger, but it tires you out -{random_stam_loss} stamina!
    """)
                break
            elif choice == "3":
                random_stam_loss = random.randint(3, 5)
                self.stamina -= random_stam_loss
                self.print(f"""[cyan]
    You stand your ground and face the creature. Bad idea! The crocodile attacks and you are forced to flee! 
    It takes a toll on your stamina! [yellow]-{random_stam_loss} stamina[/yellow].
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[cyan]
    [red]Invalid choice![/red]
    """)

        # self.print("[white]Your current health: " + str(self.health))
        # self.print("[white]Your current stamina: " + str(self.stamina))
        # self.print("[white]Your inventory: " + str(self.inventory))

    #     if self.stamina <= 0:
    #         self.health -= random.randint(2, 4)
    #         self.print("""[cyan]
    # The fight drained your [yellow]stamina[/yellow], and you lost some [red]health[/red].
    # """)
    #     elif self.stamina >= 10:
    #         self.health += random.randint(1, 3)
    #         self.print("""[cyan]
    # You handled the situation well and gained some [red]health[/red].
    # """)

    def event_three(self):
        self.print("""[cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    """)
        self.print("""[cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    """)

        while True:

            choice = self.prompt("""[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    """)
            if choice == "1":
                riddle = """[cyan]
    I speak without a mouth and hear without ears. I have no body, 
    but I come alive with wind. What am I?
    """
                answer = "echo"
                self.print("    [cyan]Riddle:")
                self.print(riddle)
                player_answer = self.prompt("   [cyan]Enter your answer: ").lower()
                if player_answer == answer:
                    health_gain = random.randint(1, 3)
                    self.health = min(self.health + health_gain, 10)  # Ensure health doesn't exceed 10
                    self.print(f"""[cyan]
    [green]Congratulations[/green]! You solved the riddle and gained [red]{health_gain} health[/red].
    """)
                    break
                else:
                    health_loss = random.randint(2, 4)
                    self.health = max(self.health - health_loss, 0)  # Ensure health doesn't go below 0
                    self.print(f"""
    Oops! Your answer is [red]incorrect[/red], and it has taken a toll on your health. [red]-{health_loss} HP[/red]!
    """)
                    break
            elif choice == "2":
                challenge_word = "challenge"
                player_word = self.prompt("""[cyan]
    Type the word '[#9D00FF]challenge[/#9D00FF]' as fast as you can: 
    challenge""").lower()
                if player_word == challenge_word:
                    stamina_gain = random.randint(2, 3)
                    self.stamina += stamina_gain
                    self.print("""
    Well done! You completed the typing challenge and gained some 
    [yellow]stamina[/yellow].
    """)
                    break
                else:
                    self.stamina -= random.randint(2, 4)
                    self.print("""[cyan]
    Oops! Your answer is [red]incorrect[/red], and it has taken 
    a toll on your [yellow]stamina[/yellow].
    """)
                    break
            elif choice == "3":
                word_to_guess = "secret"
                attempts = 3
                while attempts > 0:
                    player_guess = self.prompt("""[cyan]
    Guess the correct word: It starts with a '[green]S[/green]' and ends with a '[green]t[/green]': 
    Input""").lower()
                    if player_guess == word_to_guess:
                        # self.inventory.append(random.choice(self.items))
                        self.print("""[cyan]
    [green]Congratulations[/green]! You guessed the correct word!
    """)
                        break
                    elif player_guess != word_to_guess:
                        attempts -= 1
                        # self.stamina -= random.randint(1, 2)
                        self.print("""[white]
    [red]Incorrect[/red] guess. Try again!
    """)
                        if attempts > 0:
                            self.print(f"""[white]
    You have {attempts} attempts left.
    """)
                if attempts == 0:
                    self.stamina -= random.randint(1, 2)
                    self.print("""
    You [red]failed[/red] to guess the word. No treasure for you!
    """)
                    break
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""
    [red]Invalid choice![/red]
    """)

        # self.print("[white]Your current stamina: " + str(self.stamina))
        # self.print("[white]Your current health: " + str(self.health))
        # self.print("[white]Your inventory: " + str(self.inventory))


    # def prompt_continue(self):
    #     while True:
    #         choice = self.prompt("Type 'next' for the next challenge or 'q' to exit: ")
    #         if choice == 'next':
    #             break
    #         elif choice == 'q':
    #             exit()
    #         else:
    #             self.print("Invalid choice. Please enter 'next' or 'q'.", Fore.RED)

    # def play_game(self):
    #     self.item_collection()
    #
    #     self.print("Welcome to the River Challenge!", Fore.MAGENTA)
    #
    #     challenge_message = "You have embarked on the River Challenge! 🌊"
    #     message_length = len(challenge_message)
    #     border = "=" * (message_length + 4)
    #
    #     self.print(border, Fore.YELLOW)
    #     self.print(f"| {' ' * message_length} |", Fore.YELLOW)
    #     self.print(f"| {challenge_message} |", Fore.YELLOW)
    #     self.print(f"| {' ' * message_length} |", Fore.YELLOW)
    #     self.print(border, Fore.YELLOW)
    #
    #     events = [self.situation_event_one, self.danger_event_one, self.puzzle_event_one]
    #     random.shuffle(events)
    #
    #     for event in events[:1]:  # Play only one event
    #         event()
    #         self.print("\n")
    #
    #         if self.health <= 0 or self.stamina <= 0:
    #             self.print("Game Over! Your health or stamina has reached 0. You failed your quest.", Fore.RED)
    #             return
    #
    #     self.print("Your current health: " + str(self.health), Fore.CYAN)
    #     self.print("Your current stamina: " + str(self.stamina), Fore.CYAN)
    #     self.print("Your inventory: " + str(self.inventory), Fore.CYAN)
    #     self.print("")  # Empty line for spacing
    #     self.print("You have completed the River scenario. Well done, adventurer!", Fore.GREEN)
    #
    #     self.prompt_continue()


if __name__ == "__main__":
    # river = River()
    # river.situation_event_one()
    # river.play_game()
    # print("\n" + "=" * 50 + "\n")
    # river.danger_event_one()
    # print("\n" + "=" * 50 + "\n")
    # river.puzzle_event_one()
    from rich.console import Console
    from rich.prompt import Prompt

    console = Console()
    env = River(console.print, Prompt.ask)
    env.event_one()
