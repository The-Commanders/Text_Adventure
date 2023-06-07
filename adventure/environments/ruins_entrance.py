import random
from rich.console import Console
from adventure.consumables import *

console = Console()


class RuinsEntrance:

    def __init__(self, print, prompt):
        self.name = "River Entrance"
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]
        self.print = print
        self.prompt = prompt

    def event_one(self):
        self.print("""[#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock.
    3. Try and find the key somewhere around.""")

        while True:
            choice = self.prompt("""[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
""")
            if choice == "1":
                if "grappling hook" in self.inventory:
                    self.print("""[#FFA500]
    You managed to enter the ruins, but at a great expense. You are drained of stamina.
    """)
                    self.stamina -= 3
                    break
                else:
                    self.print(f"You do not have a grappling hook!")
                    continue
            elif choice == "2":
                self.print("""[#FFA500]
    Did you really think you would be able to pick the lock? You've made a great effort but accomplished nothing.""")
                self.stamina -= 2
                break
            elif choice == "3":
                self.print("""[#FFA500]
    That was a long and unsuccessful walk. The key is nowhere to be found, just like your energy.""")
                self.stamina -= 1
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina, self.print, self.prompt)
                continue
            else:
                continue

        # self.print("[#FFA500]Your current stamina is: :meat:", self.stamina)

    def event_two(self):
        self.print("""[#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.""")

        while True:
            choice = self.prompt("""[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    """)
            if choice == "1":
                if "survival knife" in self.inventory:
                    self.print("""[#FFA500]
    There are way too many to kill them all and they are attacking you.
    """)
                    self.health -= 4
                    break
                else:
                    self.print("""[#FFA500]You do not have a survival knife!""")
                    continue
            elif choice == "2":
                self.print("""[#FFA500]
    You are one fast runner! You've made it without loosing any health.
    """)
                self.health -= 0
                break
            elif choice == "3":
                self.print("""[#FFA500]
    You have fallen down the wall trying to climb back up and have hurt yourself.
    """)
                self.health -= 3
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina, self.print, self.prompt)
                continue
            else:
                continue

    def event_three(self):
        self.print("""[#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    We now know you posses great strength and speed. But what about your wit?
    Complete one of the following challenges to get to the next level.
    1. Solve the riddle
    2. Word association.
    3. Unscramble the word.""")

        while True:
            choice = self.prompt("""[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    """)
            if choice == "1":
                while True:
                    self.print("    [#FFA500]I’m tall when I’m young, and I’m short when I’m old.")
                    user_input = self.prompt("""[#FFA500]
        What am I? Enter your answer:
        """)
                    if user_input.lower() == "candle":
                        self.print("    [green]Correct[/green]! You've recovered some [red]health[/red] and [yellow]stamina[/yellow]")
                        # self.inventory.append(random.choice(self.items))

                        if self.health < 10:
                            self.health += 1

                        if self.stamina < 10:
                            self.stamina += 1

                        break

                    else:
                        self.print("    [red]Incorrect.")
                break
            elif choice == "2":
                self.word_association()
                break
            elif choice == "3":
              
                while True:
                    self.print("""[#FFA500]
    Unscramble the word: TNVMERONG
    """)
                    user_input = self.prompt("""[#FFA500]
    Enter your answer: 
    """)
                    if user_input.lower() == "government":
                        self.print("    [green]Correct!")
                        if self.health < 10:
                            self.health += 1

                        if self.stamina < 10:
                            self.stamina += 1

                        break
                    else:
                        self.print("""[#FFA500]
    [red]Incorrect[/red]. Looks like your unlucky this time..
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina, self.print, self.prompt)
                continue
            else:
                continue

    def word_association(self):
        words = {
            "cat": ["meow", "whiskers", "purr", "feline"],
            "dog": ["bark", "tail", "play", "canine"],
            "jungle": ["tribe", "trees", "rain", "danger"],
            "monkey": ["banana", "jungle", "tail", "steal"]
        }

        word = random.choice(list(words.keys()))
        associations = words[word]

        self.print("Think of a word associated with:", word)
        self.print("Enter your association:")

        while True:
            association = self.prompt("> ")

            if association in associations:
                self.print("    [green]Correct association!")
                self.health += 1
                self.stamina += 1
                break
            else:
                self.print("    [red]Incorrect association.")


if __name__ == "__main__":
    user_choice = RuinsEntrance()
    user_choice.event_one()
    user_choice.event_two()
    user_choice.event_three()
    from rich.console import Console
    from rich.prompt import Prompt

    console = Console()
    env = RuinsEntrance(console.print, Prompt.ask)
    env.event_one()
