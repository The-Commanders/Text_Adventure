# from consumables import use_item, item_selection
import random



class Jungle:
    def __init__(self, print, prompt):
        self.name = "Jungle"
        self.health = 8
        self.stamina = 5
        self.inventory = ['med spray', 'ration']
        self.print = print
        self.prompt = prompt
        self.description = """You arrive at the jungle, home to wildlife and indigenous tribes. Tread carefully as 
        danger could be around every corner!"""

    def event_one(self):

        self.print("""[green]
    As you are walking through the jungle, you come across a patch of thick vines 
    blocking your path. There seems to be just enough room to squeeze through, however, 
    there is no way to tell what may be inside...
    1. Try to squeeze through
    2. Find another path
    3. Cut through the vines and clear a path (requires [#9D00FF]Survival Knife[/#9D00FF])
    [/green]""")

        while True:
            selection = self.prompt("""[green]
    Pick 1, 2 or 3 or 'i' to use an item
    [/green]""")
            if selection == "1":
                rand_stam_loss = random.randint(1, 2)
                self.stamina -= rand_stam_loss
                self.print(f"""[green] 
    You try squeezing through the vines. After what seems like forever, you finally get through
    the vines and continue on your path. -[yellow]{rand_stam_loss} stamina[/yellow]!
    """)
                break
            elif selection == "2":
                rand_health_loss = random.randint(3, 5)
                self.health -= rand_health_loss
                self.print(f"""[green]
    In your search for another path, you end up stepping on a monkey trap. You free yourself and
    step on another trap. This continues for roughly an hour until you finally find a clear path..
    -[red]{rand_health_loss} HP[/red]!
    """)
                break
            elif selection == "3":
                if "survival knife" in self.inventory:
                    self.health -= 2
                    self.print(f"""[green]
    You use you knife to cut through the vines. As you are cutting a snake lands on your shoulder
    and bites you in the neck. -2 [red]HP[/red]
    """)
                    break
                else:
                    self.print("""[green]
    You do not have a [#9D00FF]survival knife[/#9D00FF] in your inventory!
    """)
                # added in to satisfy use item logic
            elif selection == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[green]
    Please pick 1, 2, or 3.
    """)

    def event_two(self):
        self.print("""[green]
    As you are walking through the jungle, you come across a pitfall trap that seems 
    to have been triggered. You peer into the trap to see the remains of a another person 
    who unfortunately triggered the trap...

    1. Jump over the trap
    2. Find another path
    3. Safely swing across the trap ([#9D00FF]requires Rope[/#9D00FF])
    """)

        while True:
            selection = self.prompt("""[green]
    Pick 1, 2 or 3 or 'i' to use an item.
    """)
            if selection == "1":
                rand_stam_loss = random.randint(1, 2)
                self.stamina -= rand_stam_loss
                rand_hp_loss = random.randint(1, 2)
                self.health -= rand_hp_loss
                self.print(f"""[green]
    You have a bad running start and as a result, you barely clear the gap
    and injure yourself a little. -[yellow]{rand_stam_loss} stamina[/yellow], -[red]{rand_hp_loss} HP[/red]! 
    """)
                break
            elif selection == "2":
                rand_health_loss = random.randint(3, 5)
                self.health -= rand_health_loss
                self.print(f"""[green]
    In your search for another path, you end up stepping on a monkey trap.
    You free yourself and step on another trap. This continues for roughly 
    an hour until you finally find a clear path.. -[red]{rand_health_loss} HP[/red]!
    """)
                break
            elif selection == "3":
                self.stamina -= 2
                self.print(f"""[green]
    With rope in hand, you toss it over a sturdy tree branch and safely swing across. -[yellow]2 stamina[/yellow]
    """)
                break
            elif selection == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("[green]Please pick 1, 2, or 3 or 'i'.")
        self.print(f"[green]Health: {self.health}[/green]\n"
              f"[yellow]Stamina: {self.stamina}[/yellow]\n"
              f"[white]Inventory: {', '.join(self.inventory)}[/white]")

    def event_three(self):
        self.print("""[green]
    You are one step closer to getting out of this dangerous jungle. This difficult journey 
    has taken a toll on your health and stamina. It hasn't been easy but you are almost there.
    To demonstrate you are worth of jumping into the next stage, you must test your wit. Please 
    complete one of the following challenges to continue.
    1. Guess the country
    2. Solve the riddle
    3. Rock, Paper, Scissor.
    """)

        while True:
            selection = self.prompt("""[green]
    Pick 1, 2 or 3
    """)
            if selection == "1":
                self.print("[white]     If I am in Barcelona...")
                user_input = self.prompt("[white]      ...in which country am I? Enter your answer:")
                if user_input.lower() == "spain":
                    self.print("""[green]
    Correct! You've recovered some health and stamina
    """)
                    self.health += 1
                    self.stamina += 1
                else:
                    self.print('[red]   Incorrect.')
            elif selection == "2":
                self.print("""[green]
    What five-letter word becomes shorter when you add two letters to it?.
    """)
                user_input = self.prompt("""[green]
    Enter your answer:
    """)
                if user_input.lower() == "short":
                    self.print("""[green]
    Correct! You've recovered some health and stamina
    """)
                    self.health += 1
                    self.stamina += 1
                else:
                    self.print("""[red]
    Incorrect.
    """)

            elif selection == "3":
                self.play_rock_paper_scissors()
            break

        self.print(f"""[green]
    Your current health is:", [red]{self.health}[/red]
    Your current stamina is: [yellow]{self.stamina}[/yellow]
    """)

    def play_rock_paper_scissors(self):
        self.print("""[green]
    Welcome to Rock, Paper, Scissors!
    """)
        choices = ["rock", "paper", "scissors"]
        player_score = 0
        monkey_score = 0

        for game_round in range(1, 4):
            self.print("    Round", game_round)
            player_choice = self.prompt("""[green]
    You have [blue]three[/blue] rounds to beat the monkey in Rock, Paper, Scissors.
            Pick 1 for rock, 2 for paper or 3 for scissors
    """)
            if player_choice not in ["1", "2", "3"]:
                self.print("""[green]
    [red]Invalid input[/red]. Please enter a number between 1 and 3.
    """)

            # convert player's choice from a string to an integer and subtract 1 from it.
            player_choice = int(player_choice) - 1
            monkey_choice = random.randint(0, 2)

            self.print(f"""
    Player chooses: {choices[player_choice]}
    Monkey chooses: {choices[monkey_choice]}
    """)

            result = self.game_winner(player_choice, monkey_choice)

            if result == "player":
                player_score += 1
                self.print("    [green]You win this round!")
            elif result == "monkey":
                monkey_score += 1
                self.print("    [red]Monkey wins this round!")
            else:
                self.print("    [blue]It's a tie!")

            self.print(f"""
    Player Score: {player_score}
    Monkey Score: {monkey_score}
    """)

        if player_score > monkey_score:
            if self.health < 10:
                self.health += 1
            if self.stamina < 10:
                self.stamina += 1
            self.print("""[green]
    Congratulations! You've beaten the monkey and recovered [yellow] 1 stamina[/yellow] and [red] 1 health[/red]!
    """)
            self.print("+1 HP, +1 SP!")
        elif player_score < monkey_score:
            rand_stam_loss = random.randint(1, 2)
            self.stamina -= rand_stam_loss
            self.print(f"Oops! Seems like the monkey beat you at Rock, Paper, Scissors and, on top of that, you lost [yellow] {rand_stam_loss} stamina[yellow]"
                  "stamina.")
        else:
            self.print("[green]It's a tie!")

    def game_winner(self, player_choice, monkey_choice):
        if player_choice == monkey_choice:
            return None

        if (player_choice == 0 and monkey_choice == 2) or \
                (player_choice == 1 and monkey_choice == 0) or \
                (player_choice == 2 and monkey_choice == 1):
            return "player"
        else:
            return "monkey"

    def event_four(self):
        self.print("""[green]
    You come across a monkey while on your journey.
    The monkey looks as if it has been entangled by the tree vines!

    1. Untangle the monkey
    2. Leave the monkey there and make fun of it
    3. Ignore the monkey and continue on your journey
    """)

        while True:
            selection = self.prompt("""[green]
    Pick 1, 2 or 3
    """)
            if selection == "1":
                rand_stam_gain = random.randint(1, 3)
                if self.stamina < 10:
                    self.stamina += rand_stam_gain
                self.print(f"""[green]
    The monkey runs and climbs up a tree and brings you a banana! +[yellow]{rand_stam_gain}[/yellow] stamina!
    """)
                break
            elif selection == "2":
                rand_health_loss = random.randint(1, 3)
                self.health -= rand_health_loss
                self.print(f"""[green]
    The monkey gets angry, and  manages to free itself! It grabs a rock nearby and throws it at you!"
    -[red]{rand_health_loss} HP[/red]!
    """)
                break
            elif selection == "3":
                self.health -= 1
                self.stamina -= 1
                self.print(f"""[green]
    You begin to walk away. As you are walking you hear the monkey screech!
    You run back to check the commotion, and you the see monkey being devoured by an anaconda.
    It is very traumatizing... -[red]1 HP[/red], -[yellow]1 stamina[/yellow]!""")
                break
            elif selection == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("""[green]
    Please pick 1, 2, or 3.
    """)


if __name__ == "__main__":
#     user_choice = Jungle()
#     user_choice.event_one()
#     user_choice.event_two()
#     user_choice.event_three()
    from rich.console import Console
    from rich.prompt import Prompt

    console = Console()
    env = Jungle(console.print, Prompt.ask)
    env.event_one()



