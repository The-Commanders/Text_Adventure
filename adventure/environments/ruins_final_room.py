import random
from rich.console import Console
from rich.style import Style
from consumables import *

console = Console()




class RuinsFinalRoom:
    def __init__(self):
        self.name = "Ruins Final Room"
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]

    def event_one(self):
        console.print("""[bold purple]
    Congratulations for making it to the final room. You've displayed great strength and wit across 
    all stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?
    """)

        console.print("""[purple]
    As you venture into the ruins you see the idol in the middle of the room. It's been carefully placed on the 
    floor right in the center. Something is off. You can feel it in your gut. You start walking very slowly towards the 
    idol, uncertain of what might happen once you get your hands on it. As you start walking towards the center of the 
    room the floor starts shaking. What is happening?? The ground starts to collapse taking the idol with it into the 
    depths. What do you do?
    """)

        console.print("""[yellow]1. Swing to safety.""")
        console.print("""[green]2. Descend to a lower level.""")
        console.print("""[blue]3. Create a bridge.""")

        while True:
            choice = input("""
    Enter your choice(1, 2, 3): 
    """)
            if choice == "1":
                console.print("""[purple]
    You throw your grappling hook into a sturdy structure above. The hook catches onto the surface and 
    you leap off the collapsing ground and swing across the room to stable ground.
    """)
                self.stamina -= 2
                break
            elif choice == "2":
                console.print("""[purple]
    You notice a lower level below, so you quickly attach your grappling hook to a secure structure and 
    start rappelling down using the rope. Carefully descending, you land safely on the lower level.
    """)
                self.stamina -= 3
                break
            elif choice == "3":
                console.print("""[purple]
    You see there are still some stable sections of ground on some sides of the chasm, so you use your 
    grappling hook and rope to create a makeshift bridge. You secure the end of the rope to a study 
    structure and throw the grappling hook to stable round on the opposite side. Once your hook catches 
    onto the ground, you tighten the create and create a stable bridge. You carefully walk across.
    """)
                self.stamina -= 3
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                print("Enter your choice(1, 2, 3): ")

        console.print("""[blue]
        Your current stamina is: :meat:""", self.stamina)

    def event_two(self):
        console.print("""[purple]
    Suddenly a cloud of smoke and dust covers everything, making it impossible to see what's happening around you. 
    When the dust settles you see it, it's the ancient guardian of the ruins. You had heard about it before, but 
    always thought it was just a myth. It seems like you will have to beat it to get the idol. What do you do?
    """)

        console.print("""[yellow]1. Create a rope trap using your grappling hook, rope and knife.""")
        console.print("""[green]2. Stealth approach and use your survival knife to attack.""")
        console.print("""[blue]3. Distract and strike with your survival knife.""")

        while True:
            choice = input("""
    Enter your choice(1, 2, 3): 
    """)

            if choice == "1":
                console.print("""[purple]
    You successfully set up the rope trap and, as expected, the guardian starts to move forward. The 
    guardian's foot catches the snare, causing it to stumble and lose balance. Seizing this opportunity, 
    you rush forward and attack the vulnerable area on the guardian's back with your survival knife. The 
    guardian lets out a roar of pain and temporarily loses focus, giving you 
    a chance to deal further damage.""")
                self.health -= 3
                break
            elif choice == "2":
                console.print("""[purple]
    You successfully reach a position near the guardian's vulnerable spot without being detected. You 
    unleash a swift and precise attack, driving your survival knife into the weak area. The guardian lets 
    out a roar of pain, but it remains standing. Realizing that you have a limited window of opportunity, 
    you must act quickly and retreat to cover before the guardian retaliates. You return to the shadows, 
    evading the guardian's gaze and avoiding its powerful attacks.""")
                self.health -= 3
                break
            elif choice == "3":
                console.print("""[purple]
    You pick a small stone from the ground and hurl it to a corner of the room, away from your intended 
    path. The guardian, being vigilant, turns its head toward the sound and moves away from its original 
    position, temporarily distracted by the false threat. You take advantage of this opportunity to move 
    swiftly and silently towards the guardian. With your survival knife you strike a powerful attack to the 
    guardian's weak spot. The guardian lets out a roar of pain and dies.""")
                self.health -= 1
                break
            elif choice == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue
            else:
                print("Enter your choice(1, 2, 3): ")

        console.print("""[blue]
    Your current health is: :heart:""", self.health)

    def event_three(self):
        console.print("""[purple]
    As the echoes of battle subside, the ruins' atmosphere takes on an eerie calmness. Your gaze shifts towards the 
    center of the final room, where a magnificent pedestal starts to rise from the ground. It is mesmerizing. 
    Adorned with ancient inscriptions and symbols. It becomes clear that the last obstacle standing between you and 
    the idol is an intricate puzzle, requiring both intellect and intuition to unravel. Complete the following two 
    challenges to obtain the idol.
    """)

        console.print("""[yellow]1. Guess the number.""")
        console.print("""[green]2. Play hangman.""")

        while True:
            selection = input("Enter your choice(1, 2)")
            if selection == "1":
                self.guess_number()
                break
            elif selection == "2":
                self.play_hangman()
                break
            elif selection == "i":
                self.health, self.stamina = item_selection(self.inventory, self.health, self.stamina)
                continue

            # if option1_completed and option2_completed:
            #     print("Congratulations! You have successfully obtained the long-lost idol, a priceless artifact hidden "
            #           "within the depths of the ancient ruins. As you hold it in your hands, a surge of power and "
            #           "accomplishment courses through your veins. You emerge from the treacherous depths, the idol "
            #           "shining brightly in your grasp, ready to share the tales of your daring adventure with those "
            #           "who await your triumphant return. The game concludes, but your legend will live on.")
            
            
    def guess_number(self):
        console.print("""[purple]
    Welcome to Guess the Number!
    """)
        secret_number = random.randint(1, 100)
        max_attempts = 8
        attempts = 0

        while attempts < max_attempts:
            guess = int(input("Guess a number between 1 and 100. You have 8 attempts:"))
            attempts += 1

            if guess < secret_number:
                console.print("""[purple]
    The number you've entered is too low!
    """)
            elif guess > secret_number:
                console.print("""[purple]
    The number you've entered is too high!
    """)
            else:
                console.print("""[purple]
    Congratulations! You've guessed the number!""")
                break

            if attempts == max_attempts:
                console.print("""[green]
    Game Over!""")

    def play_hangman(self):
        console.print("""[purple]
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

            console.print("""[purple]
    Guess the word:""", hidden_word)
            console.print("""[purple]
    Attempts remaining:""", attempts)
            console.print(hangman_representation[8 - attempts])

            if hidden_word == chosen_word:
                console.print("""[purple]
    Congratulations! You guessed the word correctly.""")
                break

            if attempts == 0:
                console.print("""[purple]
    Game over! You ran out of attempts. The word was:""", chosen_word)
                break

            guess = input("""Enter a letter: """).lower()

            if len(guess) != 1 or not guess.isalpha():
                console.print("""[purple]
    Invalid input! Please enter a single letter.""")
                continue

            if guess in guessed_letters:
                console.print("""[purple]
    You already guessed that letter.""")
            else:
                guessed_letters.append(guess)
                if guess in chosen_word:
                    console.print("""[purple]
    Correct guess!""")
                else:
                    console.print("""[purple]
    Wrong guess!""")
                    attempts -= 1

            console.print()


if __name__ == "__main__":
    user_choice = RuinsFinalRoom()
    user_choice.event_one()
    user_choice.event_two()
    user_choice.event_three()
