import random


class River:
    def __init__(self, name):
        self.name = name
        self.stamina = 10
        self.health = 10
        self.inventory = []

    def event_one(self):
        print("You come across a river. What do you do?")
        print("1. Attempt to swim across the river.")
        print("2. Build a makeshift raft to cross the river.")
        print("3. Follow the riverbank to search for a bridge or easier crossing point.")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            self.stamina -= random.randint(3, 5)
            print("You attempt to swim across the river. The strong current drains your stamina.")
        elif choice == '2':
            self.stamina -= random.randint(1, 3)
            print("You build a makeshift raft and cross the river safely, but it takes some effort.")
        elif choice == '3':
            self.stamina -= random.randint(1, 2)
            print("You decide to follow the riverbank and find an easier crossing point, but it still tires you out.")
        else:
            print("Invalid choice.")

        print("Your current health:", self.health)
        print("Your current stamina:", self.stamina)
        print("Your inventory:", self.inventory)

    def event_two(self):
        print("You encounter a dangerous situation. What do you do?")
        print("1. Confront the threat head-on.")
        print("2. Try to evade the danger stealthily.")
        print("3. Retreat and seek a safer route.")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            self.stamina -= random.randint(2, 4)
            print("You bravely confront the danger, but it takes a toll on your stamina.")
        elif choice == '2':
            self.stamina -= random.randint(1, 3)
            print("You attempt to evade the danger stealthily. It requires some effort but helps conserve your stamina.")
        elif choice == '3':
            self.stamina -= random.randint(1, 2)
            print("You decide to retreat and find a safer route, but it still tires you out.")
        else:
            print("Invalid choice.")

        print("Your current health:", self.health)
        print("Your current stamina:", self.stamina)
        print("Your inventory:", self.inventory)

    def event_three(self):
        print("You come across a mysterious puzzle. What do you do?")
        print("1. Solve a riddle.")
        print("2. Complete a typing challenge.")
        print("3. Guess the correct word.")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
            answer = "echo"
            print("Riddle:", riddle)
            player_answer = input("Enter your answer: ").lower()
            if player_answer == answer:
                self.health = min(self.health + random.randint(1, 3), 10)  # Ensure health doesn't exceed 10
                print("Congratulations! You solved the riddle and gained some health.")
            else:
                self.health = max(self.health - random.randint(2, 4), 0)  # Ensure health doesn't go below 0
                print("Oops! Your answer is incorrect, and it has taken a toll on your health.")
        elif choice == '2':
            challenge_word = "challenge"
            player_word = input("Type the word 'challenge' as fast as you can: ").lower()
            if player_word == challenge_word:
                self.stamina -= random.randint(1, 3)
                print("Well done! You completed the typing challenge and gained some stamina.")
            else:
                self.stamina -= random.randint(2, 4)
                print("Oops! Your answer is incorrect, and it has taken a toll on your stamina.")
        elif choice == '3':
            word_to_guess = "secret"
            attempts = 3
            while attempts > 0:
                player_guess = input("Guess the correct word: It starts with a 'S' and ends with a 't': ").lower()
                if player_guess == word_to_guess:
                    self.inventory.append("treasure")
                    print("Congratulations! You guessed the correct word")
                    break
                else:
                    attempts -= 1
                    self.stamina -= random.randint(1, 2)
                    print("Incorrect guess. Try again!")
                    if attempts > 0:
                        print(f"You have {attempts} attempts left.")
            else:
                print("You failed to guess the word. No treasure for you!")

        print("Your current stamina:", self.stamina)
        print("Your current health:", self.health)
        print("Your inventory:", self.inventory)

    def play_random_event(self):
        event = random.choice([self.event_one, self.event_two, self.event_three])
        event()


river = River("Example River")
river.play_random_event()
# while True:
#     choice = input("Enter 's' to start your journey or 'q' to quit: ")
#
#     if choice.lower() == 's':
#         river.play_random_event()
#     elif choice.lower() == 'q':
#         break
#     else:
#         print("Invalid choice.")
