import random
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
# from adventure.consumables import *

console = Console()


class RuinsFinalRoom:
    def __init__(self, print, prompt):
        self.name = "Ruins Final Room"
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.print = print
        self.prompt = prompt

    def event_one(self):
        self.print("""[bold purple]
    Congratulations for making it to the final room. You've displayed great strength and wit across 
    all stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?
    """)

        self.print("""[purple]
    Stepping into the final room ready to face your final challenge, you notice somethings off. The idol stands
    before you. Proceeding carefully, you grab the idol on the desk before you. Examining the idol before you,
    you notice writing on the base reading "[i yellow]MADE IN CHINA[/i yellow]". Of course it wouldn't be this
    easy, the floor caves in from below you, you must think quickly!
        What do you do?
    1. Leap of faith
    2. Grab the side ledge
    3. Jump over the ledge, find a new way through
    """)

        while True:
            choice = self.prompt("""[purple]
    Enter your choice(1, 2, 3) 
    """)
            if choice == "1":
                self.stamina -= 2
                self.health -= 2
                self.print("""[purple]
    Your first reaction is to trust the fall, weird but ok? You fall for a few seconds,
    expecting to break a bone or 2, but somehow you land in a convenient hay stack. Thats
    just what you needed! Not the smartest decision, as you take -2 [red]health[/red] and [yellow]stamina[/yellow].
    You continue on to the idols room.
    """)
                break
            elif choice == "2":
                self.stamina -= 2
                self.print("""[purple]
    Quickly thinking, you grab the side ledge before falling into the abyss. That was way too
    close! Your quick save costed -2 [yellow]stamina[/yellow], but better than breaking a leg
    in an ancient temple. You continue on to the idol room.
    """)
                break
            elif choice == "3":
                self.print("""[purple]
    Mustering up all your strength, you make the jump too the opposite side, loosing your footing
    for a second, you catch yourself. With a brief sigh of relief, and continue your search for a
    MUCH safer route downwards.
    """)
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina, self.print,
                                                           self.prompt)
                continue
            else:
                self.print("Enter your choice(1, 2, 3): ")

    def event_two(self):
        self.print("""[purple]
    Stepping into the final room, you feel uneasy. Its just a regular room, nothing special. You feel the ground
    starting to shake underneath you and rocks start to form into the shape of a figure, creating a huge guardian.
    The guardian turns to you with its eyes flashing [red]red[/red], not good! 
    What do you do?
    1. Create a rope trap using your rope and escape
    2. Stealth approach and use your survival knife to attack.
    3. Distract and strike with rocks.
    """)

        while True:
            choice = self.prompt("""
    Enter your choice(1, 2, 3): 
    """)

            if choice == "1":
                self.print("""[purple]
    You successfully set up the rope trap and, as expected, the guardian starts to move forward. The 
    guardian's foot catches the snare, causing it to stumble and lose balance. Seizing this opportunity, 
    you escape the room but you cut your shoulder on the way out, -2 [red]health[/red].""")
                self.health -= 2
                break
            elif choice == "2":
                if "survival knife" in self.inventory:
                    self.print("""[purple]
    You successfully reach a position near the guardian's vulnerable spot without being detected. You 
    unleash a swift and precise attack, driving your survival knife into its weak area. The guardian lets 
    out a roar of pain and dies.""")
                    self.health -= 0
                    break
                else:
                    self.print("""
    [purple]You do not have a [#1F51FF]survival knife[/#1F51FF]!""")
                    continue
            elif choice == "3":
                self.print("""[purple]
    You pick a small stone from the ground and hurl it to a corner of the room, away from your intended 
    path. The guardian, being vigilant, turns its head toward the sound and moves away from its original 
    position, temporarily distracted by the false threat. You take advantage of this opportunity to move 
    swiftly and silently towards the guardian. You strike various powerful attacks to the guardian's weak spot with 
    rocks you pick from the ground. The guardian lets out a roar of pain and dies.""")
                self.health -= 1
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                self.print("Enter your choice(1, 2, 3): ")

    def event_three(self):
        self.print("""[purple]
    As you step into the final room, you hear a voice echoing throughout the room. "Hello adventurer, let's see if  
    you are worthy, step forward and pick a challenge".
    You step forward and read on the wall...
    1. Guess the number.
    2. Play hangman.
    """)

        while True:
            selection = Prompt.ask("""
    Enter your choice(1, 2)
    """)
            if selection == "1":
                self.guess_number()
                break
            elif selection == "2":
                self.play_hangman()
                break
            elif selection == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            
    def guess_number(self):
        self.print("""[purple]
    Welcome to Guess the Number!
    """)
        secret_number = random.randint(1, 100)
        max_attempts = 8
        attempts = 0

        while attempts < max_attempts:
            guess = int(self.prompt("Guess a number between 1 and 100. You have 8 attempts:"))
            attempts += 1

            if guess < secret_number:
                self.print("""[purple]
    The number you've entered is too low!
    """)
            elif guess > secret_number:
                self.print("""[purple]
    The number you've entered is too high!
    """)
            else:
                self.print("""[purple]
    Congratulations! You've guessed the number!""")
                break

            if attempts == max_attempts:
                self.print("""[green]
    Game Over!""")

    def play_hangman(self):
        self.print("""[purple]
    Welcome to Hangman!
    """)
        words = ['treasure', 'secret', 'adventure', 'artifact', 'level', 'winner']
        chosen_word = random.choice(words)
        guessed_letters = []
        attempts = 9
        hangman_representation = [
            '''
                ____
               |    |
                    |
                    |
                    |
                    |
            ''',
            '''
               ____
              |    |
              O    |
                   |
                   |
                   |
            ''',
            '''
               ____
              |    |
              O    |
              |    |
                   |
                   |
            ''',
            '''
               ____
              |    |
              O    |
             /|    |
                   |
                   |
            ''',
            '''
               ____
              |    |
              O    |
             /|\\   |
                   |
                   |
            ''',
            '''
               ____
              |    |
              O    |
             /|\\   |
              |    |
                   |
    
            ''',
            '''
               ____
              |    |
              O    |
             /|\\   |
              |    |
              |    |
                   |
    
            ''',
            '''
              ____
             |    |
             O    |
            /|\\   |
             |    |
             |    |
            /     |
            ''',
            '''
              ____
             |    |
             O    |
            /|\\   |
             |    |
             |    |
            / \\   |
                  |
            
            '''
        ]
        while True:
            hidden_word = ''
            for letters in chosen_word:
                if letters in guessed_letters:
                    hidden_word += letters
                else:
                    hidden_word += '_ '

            self.print("""[purple]
    Guess the word:""", hidden_word)
            self.print("""[purple]
    Attempts remaining:""", attempts)
            self.print(hangman_representation[8 - attempts])

            if hidden_word == chosen_word:
                self.print("""[bold blue]
    Congratulations! You guessed the word correctly.""")
                break

            if attempts == 0:
                self.print("""[purple]
    Game over! You ran out of attempts. The word was:""", chosen_word)
                break

            guess = Prompt.ask("""
    Enter a letter: 
    """).lower()

            if len(guess) != 1 or not guess.isalpha():
                self.print("""[purple]
    Invalid input! Please enter a single letter.""")
                continue

            if guess in guessed_letters:
                self.print("""[purple]
    You already guessed that letter.""")
            else:
                guessed_letters.append(guess)
                if guess in chosen_word:
                    self.print("""[purple]
    Correct guess!""")
                else:
                    self.print("""[purple]
    Wrong guess!""")
                    attempts -= 1

            self.print()


if __name__ == "__main__":
    from rich.console import Console
    from rich.prompt import Prompt
    console = Console()

    env = RuinsFinalRoom(console.print, Prompt.ask)
    env.event_one()
    env.event_two()
    env.event_three()

