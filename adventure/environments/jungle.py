import random


class Jungle:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.description = """You arrive at the jungle, home to wildlife and indigenous tribes. Tread carefully as danger
        could be around every corner!"""

    def event_one(self):

        print("As you are walking through the jungle, you come across a patch of thick patch of vine blocking your path.")
        print("There seems to be just enough room to squeeze through, however, there is no way to tell what may be inside...")

        print("1. Try to squeeze through ")
        print("2. Find another path")
        print("3. Cut through the vines and clear a path (requires Survival Knife)")

        while True:
            selection = input("Pick 1, 2 or 3\n>")
            if selection == "1":
                rand_stam_loss = random.randint(1, 2)
                self.health -= rand_stam_loss
                print(f" You try squeezing through the vines. After what seems like forever, you finally get through"
                      f"the vines and continue on your path. -{rand_stam_loss} stamina! ")
                break
            elif selection == "2":
                rand_health_loss = random.randint(3, 5)
                self.health -= rand_health_loss
                print(f"In your search for another path, you end up stepping on a monkey trap. You free yourself and "
                      f"step on another trap. This continues for roughly an hour until you finally find a clear path.."
                      f" -{rand_health_loss} HP!")
                break
            elif selection == "3":
                self.health -= 2
                print(f"You use you knife to cut through the vines. As you are cutting a snake lands on your shoulder"
                      f"and bites you in the neck. -2 HP")
                break
            else:
                print("Please pick 1, 2, or 3.")

    def event_two(self):
        print("As you are walking through the jungle, you come across a pitfall trap that seems to have been triggered.")
        print("You peer into the trap to see the remains of a another person who unfortunately triggered the trap...")

        print("1. Jump over the trap")
        print("2. Find another path")
        print("3. Safely swing across the trap (requires Rope)")

        while True:
            selection = input("Pick 1, 2 or 3\n>")
            if selection == "1":
                rand_stam_loss = random.randint(1, 2)
                self.stamina -= rand_stam_loss
                rand_hp_loss = random.randint(1, 2)
                self.health -= rand_hp_loss
                print(f"You have a bad running start and as a result, you barely clear the gap "
                      f" and injure yourself a little. -{rand_stam_loss} stamina, -{rand_hp_loss} HP! ")
                break
            elif selection == "2":
                rand_health_loss = random.randint(3, 5)
                self.health -= rand_health_loss
                print(f"In your search for another path, you end up stepping on a monkey trap. You free yourself and "
                      f"step on another trap. This continues for roughly an hour until you finally find a clear path.."
                      f" -{rand_health_loss} HP!")
                break
            elif selection == "3":
                self.stamina -= 2
                print(f"With rope in hand, you toss it over to sturdy tree branch and safely swing across. ")
                break
            else:
                print("Please pick 1, 2, or 3.")

    def event_three(self):
        print("You come across a monkey while on your journey. The monkey looks as if it has been entangled by the tree vines!")

        print("1. Untangle the monkey")
        print("2. Leave the monkey there and make fun of it!")
        print("3. Ignore the monkey and continue on your journey")

        while True:
            selection = input("Pick 1, 2 or 3\n>")
            if selection == "1":
                rand_stam_gain = random.randint(1,3)
                if self.stamina < 10:
                    self.stamina += rand_stam_gain
                print(f"The monkey runs and climbs up a tree and brings you a banana! +{rand_stam_gain} stamina!")
                break
            elif selection == "2":
                rand_health_loss = random.randint(1,3)
                self.health -= rand_health_loss
                print("The monkey gets angry, and  manages to free itself! It grabs a rock nearby and throws it at you!"
                      f" -{rand_health_loss} HP!")
                break1
            elif selection == "3":
                self.health -= 1
                self.stamina -= 1
                print("You begin to walk away. As you are walking you hear the monkey screech! You run back to check the"
                      f"commotion, and you the see monkey being devoured by an anaconda. It is very traumatizing... -1 HP, -1 stamina!")
                break
            else:
                print("Please pick 1, 2, or 3.")


