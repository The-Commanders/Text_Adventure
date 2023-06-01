import random
from colorama import Fore, Style


class River:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["First aid spray", "Ration"]


    def display_text(self, text, color=None):
        if color:
            print(color + text + Fore.RESET)
        else:
            print(text)

    def item_collection(self):
        self.display_text("Items in the game:", Fore.CYAN)
        for item in self.items:
            self.display_text("- " + item, Fore.CYAN)

    def situation_event_one(self):
        self.display_text("You come across a wide river. How do you proceed?", Fore.CYAN)
        self.display_text("1. Swim across the river.", Fore.CYAN)
        self.display_text("2. Build a makeshift raft and sail across.", Fore.CYAN)
        self.display_text("3. Look for a bridge upstream.", Fore.CYAN)

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice < 1 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                self.display_text("Invalid choice. Please enter a number between 1 and 3.", Fore.RED)

        if choice == 1:
            self.stamina -= random.randint(1, 3)
            self.display_text("You swim across the river. It was tiring, and you lost some stamina.", Fore.YELLOW)
        elif choice == 2:
            self.inventory.append("Raft")
            self.display_text("You build a makeshift raft and sail across the river. You now have a raft in your inventory.", Fore.GREEN)
        elif choice == 3:
            self.stamina -= random.randint(1, 2)
            self.display_text("You find a bridge upstream and cross the river safely, but it tires you out a bit.", Fore.YELLOW)
        else:
            self.display_text("Invalid choice. Please enter a number between 1 and 3.", Fore.RED)

        self.display_text("Your current health: " + str(self.health), Fore.CYAN)
        self.display_text("Your current stamina: " + str(self.stamina), Fore.CYAN)
        self.display_text("Your inventory: " + str(self.inventory), Fore.CYAN)

        if self.stamina <= 0:
            self.health -= random.randint(2, 4)
            self.display_text("The swim drained your stamina, and you lost some health.", Fore.RED)
        elif self.stamina >= 10:
            self.health += random.randint(1, 3)
            self.display_text("You handled the swim well and gained some health.", Fore.GREEN)

        self.prompt_continue()

    def danger_event_one(self):
        self.display_text("You encounter a dangerous creature. What do you do?", Fore.CYAN)
        self.display_text("1. Fight the creature.", Fore.CYAN)
        self.display_text("2. Try to evade the danger.", Fore.CYAN)
        self.display_text("3. Stand your ground.", Fore.CYAN)

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice < 1 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                self.display_text("Invalid choice. Please enter a number between 1 and 3.", Fore.RED)

        if choice == 1:
            self.stamina -= random.randint(2, 4)
            self.display_text("You engage in a fierce battle. The creature hits you, and you lose some stamina.",
                              Fore.RED)
        elif choice == 2:
            self.stamina -= random.randint(1, 3)
            self.display_text("You manage to evade the danger, but it tires you out.", Fore.YELLOW)
        elif choice == 3:
            self.stamina -= random.randint(1, 2)
            self.display_text("You stand your ground and face the creature. It takes a toll on your stamina.",
                              Fore.YELLOW)
        else:
            self.display_text("Invalid choice. Please enter a number between 1 and 3.", Fore.RED)

        self.display_text("Your current health: " + str(self.health), Fore.CYAN)
        self.display_text("Your current stamina: " + str(self.stamina), Fore.CYAN)
        self.display_text("Your inventory: " + str(self.inventory), Fore.CYAN)

        if self.stamina <= 0:
            self.health -= random.randint(2, 4)
            self.display_text("The fight drained your stamina, and you lost some health.", Fore.RED)
        elif self.stamina >= 10:
            self.health += random.randint(1, 3)
            self.display_text("You handled the situation well and gained some health.", Fore.GREEN)

        self.prompt_continue()

    def puzzle_event_one(self):
        self.display_text("You come across a mysterious puzzle. What do you do?", Fore.CYAN)
        self.display_text("1. Solve a riddle.", Fore.CYAN)
        self.display_text("2. Complete a typing challenge.", Fore.CYAN)
        self.display_text("3. Guess the correct word.", Fore.CYAN)

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice < 1 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                self.display_text("Invalid choice. Please enter a number between 1 and 3.", Fore.RED)

        if choice == 1:
            riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
            answer = "echo"
            self.display_text("Riddle:", Fore.YELLOW)
            self.display_text(riddle, Fore.YELLOW)
            player_answer = input("Enter your answer: ").lower()
            if player_answer == answer:
                self.health = min(self.health + random.randint(1, 3), 10)  # Ensure health doesn't exceed 10
                self.display_text("Congratulations! You solved the riddle and gained some health.", Fore.GREEN)
            else:
                self.health = max(self.health - random.randint(2, 4), 0)  # Ensure health doesn't go below 0
                self.display_text("Oops! Your answer is incorrect, and it has taken a toll on your health.", Fore.RED)
        elif choice == 2:
            challenge_word = "challenge"
            player_word = input("Type the word 'challenge' as fast as you can: ").lower()
            if player_word == challenge_word:
                self.stamina -= random.randint(1, 3)
                self.display_text("Well done! You completed the typing challenge and gained some stamina.", Fore.GREEN)
            else:
                self.stamina -= random.randint(2, 4)
                self.display_text("Oops! Your answer is incorrect, and it has taken a toll on your stamina.", Fore.RED)
        elif choice == 3:
            word_to_guess = "secret"
            attempts = 3
            while attempts > 0:
                player_guess = input("Guess the correct word: It starts with a 'S' and ends with a 't': ").lower()
                if player_guess == word_to_guess:
                    self.inventory.append(random.choice(self.items))
                    self.display_text("Congratulations! You guessed the correct word", Fore.GREEN)
                    break
                else:
                    attempts -= 1
                    self.stamina -= random.randint(1, 2)
                    self.display_text("Incorrect guess. Try again!", Fore.RED)
                    if attempts > 0:
                        self.display_text(f"You have {attempts} attempts left.", Fore.RED)
            else:
                self.display_text("You failed to guess the word. No treasure for you!", Fore.RED)

        self.display_text("Your current stamina: " + str(self.stamina), Fore.CYAN)
        self.display_text("Your current health: " + str(self.health), Fore.CYAN)
        self.display_text("Your inventory: " + str(self.inventory), Fore.CYAN)

        self.prompt_continue()

    def prompt_continue(self):
        while True:
            choice = input("Type 'next' for the next challenge or 'q' to exit: ")
            if choice == 'next':
                break
            elif choice == 'q':
                exit()
            else:
                self.display_text("Invalid choice. Please enter 'next' or 'q'.", Fore.RED)

    def play_game(self):
        self.item_collection()

        self.display_text("Welcome to the River Challenge!", Fore.MAGENTA)

        challenge_message = "You have embarked on the River Challenge! 🌊"
        message_length = len(challenge_message)
        border = "=" * (message_length + 4)

        self.display_text(border, Fore.YELLOW)
        self.display_text(f"| {' ' * message_length} |", Fore.YELLOW)
        self.display_text(f"| {challenge_message} |", Fore.YELLOW)
        self.display_text(f"| {' ' * message_length} |", Fore.YELLOW)
        self.display_text(border, Fore.YELLOW)

        events = [self.situation_event_one, self.danger_event_one, self.puzzle_event_one]
        random.shuffle(events)

        for event in events[:1]:  # Play only one event
            event()
            self.display_text("\n")

            if self.health <= 0 or self.stamina <= 0:
                self.display_text("Game Over! Your health or stamina has reached 0. You failed your quest.", Fore.RED)
                return

        self.display_text("Your current health: " + str(self.health), Fore.CYAN)
        self.display_text("Your current stamina: " + str(self.stamina), Fore.CYAN)
        self.display_text("Your inventory: " + str(self.inventory), Fore.CYAN)
        self.display_text("")  # Empty line for spacing
        self.display_text("You have completed the River scenario. Well done, adventurer!", Fore.GREEN)

        self.prompt_continue()


if __name__ == "__main__":
    river = River("Amazon")
    river.situation_event_one()
    river.play_game()
    print("\n" + "=" * 50 + "\n")
    river.danger_event_one()
    print("\n" + "=" * 50 + "\n")
    river.puzzle_event_one()
