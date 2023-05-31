from adventure.game import *


class RuinsFinalRoom():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]

    def event_one(self):
        print("Congratulations for making it to the final room. You've displayed great strength and wit across all "
              "stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?")
        print("As you walk into the final room  ")
        print("1. Climb the wall using your grappling hook.")
        print("2. Try and pick the lock with your survival knife")
        print("3. Try and find the key somewhere around.")











    print("You come across a monkey while on your journey. The monkey looks as if it has been entangled by the "
          "tree vines!")

    print("1. Untangle the monkey")
    print("2. Leave the monkey there and make fun of it!")
    print("3. Ignore the monkey and continue on your journey")

    while True:
        selection = input("Pick 1, 2 or 3\n>")
        if selection == "1":
            rand_stam_gain = random.randint(1, 3)
            if self.stamina < 10:
                self.stamina += rand_stam_gain
            print(f"The monkey runs and climbs up a tree and brings you a banana! +{rand_stam_gain} stamina!")
            break
        elif selection == "2":
            rand_health_loss = random.randint(1, 3)
            self.health -= rand_health_loss
            print("The monkey gets angry, and  manages to free itself! It grabs a rock nearby and throws it at you!"
                  f" -{rand_health_loss} HP!")
            break
        elif selection == "3":
            self.health -= 1
            self.stamina -= 1
            print("You begin to walk away. As you are walking you hear the monkey screech! You run back to check "
                  "the"
                  f"commotion, and you the see monkey being devoured by an anaconda. It is very traumatizing... "
                  f"-1 HP, -1 stamina!")
            break
        else:
            print("Please pick 1, 2, or 3.")
