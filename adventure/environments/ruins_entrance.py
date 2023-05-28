from adventure.game import *


class RuinsEntrance:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]

    def event_one(self):
        print("Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in "
              "order to get your hands on it you will have to test your strength and wit a few more times.")
        print("It seems like the door to get into the ruins is closed and you don't have the key. How would you like"
              "to proceed in order to gain access to the ruins? ")
        print("1. Climb the wall using your grappling hook.")
        print("2. Try and pick the lock with your survival knife")
        print("3. Try and find the key somewhere around.")

        while True:
            choice = input("Enter your choice(1, 2, 3): ")
            if choice == "1":
                print("You managed to enter the ruins, but at a great expense. You are drained of stamina.")
                self.stamina -= 3
            elif choice == "2":
                print("Did you really think you would be able to pick the lock? You've made a great effort but "
                      "accomplished nothing.")
                self.stamina -= 2
            elif choice == "3":
                print("That was a long and unsuccessful walk. The key is nowhere to be found, just as your energy.")
                self.stamina -= 1
            break

        print("Your current stamina is:", self.stamina)

    def event_two(self):
        print("As you jump into the ruins, you find yourself surrounded by scorpions. What do you do?")
        print("1. Try to kill them with your survival knife.")
        print("2. Run as fast as you can into the ruins so they don't catch you.")
        # print("3. Climb the wall back out.")

        while True:
            choice = input("Enter your choice(1, 2, 3): ")
            if choice == "1":
                print("There are way too many to kill them all and they are attacking you.")
                self.health -= 4
            elif choice == "2":
                print("You are one fast runner! You've made it without loosing any health.")
                self.health -= 0
            # elif choice == "3":
                # print("You have fallen down the wall trying to climb back up and have hurt yourself.")
                # self.health -= 3
            break

        print("Your current health is:", self.health)

    def event_three(self):
        print("We now know you posses great strength and speed. But what about your wit? Complete one of the following "
              "challenges to get to the next level")
        print("1. Solve the riddle")
        print("2. Guess the country.")
        print("3. Unscramble the word.")

        while True:
            choice = input("Enter your choice(1, 2, 3): ")
            if choice == "1":
                print("I’m tall when I’m young, and I’m short when I’m old.")
                user_input = input("What am I? Enter your answer:")
                if user_input.lower() == "candle":
                    print("Correct! You've recovered some health and stamina")
                    self.health += 1
                    self.stamina += 1
                else:
                    print("Incorrect.")
            elif choice == "2":
                print("If I am in Barcelona...")
                user_input = input("...in which country am I? Enter your answer:")
                if user_input.lower() == "spain":
                    print("Correct! You've recovered some health and stamina")
                    self.health += 1
                    self.stamina += 1
                else:
                    print("Incorrect.")
            elif choice == "3":
                print("Unscramble the word: LGOVNEIRNEMT")
                user_input = input("Enter your answer: ")
                if user_input.lower() == "government":
                    print("Correct!")
                    self.health += 1
                    self.stamina += 1
                else:
                    print("Incorrect. You've recovered some health and stamina")
            break

        print("Your current health is:", self.health)
        print("Your current stamina is:", self.stamina)


if __name__ == "__main__":
    user_choice = RuinsEntrance("Ruins Entrance")
    user_choice.event_one()
    user_choice.event_two()
    user_choice.event_three()


