import random
from colorama import Fore, Style

class Ruins_Halls:
    def __init__(self, name):
        self.name = name
        self.stamina = 10
        self.health = 10
        self.inventory = []

    def display_text(self, text, color=None):
        if color:
            print(color + text + Fore.RESET)
        else:
            print(text)

    def situation_event_one(self):
        print(Fore.CYAN + "You encounter a mysterious artifact. What do you do?" + Style.RESET_ALL)
        self.display_text("1. Inspect the artifact closely.", Fore.CYAN)
        self.display_text("2. Leave the artifact alone.", Fore.CYAN)
        self.display_text("3. Take the artifact with you.", Fore.CYAN)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            self.stamina -= random.randint(1, 2)
            print(Fore.GREEN + "You carefully inspect the artifact and find a hidden compartment. Inside, you discover a valuable gem. Your stamina decreases slightly." + Style.RESET_ALL)
            self.inventory.append("Valuable Gem")
        elif choice == '2':
            print(Fore.YELLOW + "You decide to leave the artifact undisturbed and continue your journey." + Style.RESET_ALL)
        elif choice == '3':
            self.stamina -= random.randint(2, 3)
            print(Fore.GREEN + "You decide to take the artifact with you, but it's heavy and tires you out. Your stamina decreases." + Style.RESET_ALL)
            self.inventory.append("Mysterious Artifact")
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 3." + Style.RESET_ALL)
            self.situation_event_one()

    def danger_event_one(self):
        print(Fore.CYAN + "You stumble upon a hidden trap. What do you do?" + Style.RESET_ALL)
        self.display_text("1. Try to disarm the trap.", Fore.CYAN)
        self.display_text("2. Jump over the trap.", Fore.CYAN)
        self.display_text("3. Go back the way you came.", Fore.CYAN)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            self.health -= random.randint(2, 3)
            print(Fore.RED + "You attempt to disarm the trap but trigger it instead. You get injured, and your health decreases." + Style.RESET_ALL)
        elif choice == '2':
            self.stamina -= random.randint(1, 2)
            print(Fore.GREEN + "You muster all your agility and successfully jump over the trap. Your stamina decreases slightly." + Style.RESET_ALL)
        elif choice == '3':
            self.stamina -= random.randint(1, 2)
            print(Fore.YELLOW + "You decide it's best to go back the way you came and avoid the trap altogether. Your stamina decreases slightly." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 3." + Style.RESET_ALL)
            self.danger_event_one()

    def puzzle_event_one(self):
        print(Fore.CYAN + "You come across a locked door. What do you do?" + Style.RESET_ALL)
        self.display_text("1. Look for a key to unlock the door.", Fore.CYAN)
        self.display_text("2. Attempt to pick the lock.", Fore.CYAN)
        self.display_text("3. Find an alternative route.", Fore.CYAN)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            self.stamina -= random.randint(1, 2)
            print(Fore.GREEN + "You search the surroundings and find a key hidden nearby. Your stamina decreases slightly." + Style.RESET_ALL)
            self.inventory.append("Door Key")
        elif choice == '2':
            self.health -= random.randint(2, 3)
            print(Fore.RED + "You try to pick the lock but accidentally break your lockpick. In the process, you injure yourself, and your health decreases." + Style.RESET_ALL)
        elif choice == '3':
            self.stamina -= random.randint(1, 2)
            print(Fore.YELLOW + "You decide to find an alternative route and discover a hidden passage that leads past the locked door. Your stamina decreases slightly." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 3." + Style.RESET_ALL)
            self.puzzle_event_one()

    def play_game(self):
        self.display_text("Welcome to the Adventure Game!", Fore.MAGENTA)

        challenge_message = "You have entered the Ruin Halls Challenge! 🏰"
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
        self.display_text("You have completed the Ruin Halls scenario. Well done, adventurer!", Fore.GREEN)

ruin_halls = Ruins_Halls("Ruin Halls")
ruin_halls.play_game()

# Add the following code to prompt the user for the next challenge or to exit
# next_challenge = input("Type 'next' for the next challenge or 'q' to exit: ")
# while next_challenge.lower() != 'q':
#     ruin_halls.play_game()
#     next_challenge = input("Type 'next' for the next challenge or 'q' to exit: ")

# Exit the game
print(Fore.GREEN + "Thank you for playing the game!" + Style.RESET_ALL)



