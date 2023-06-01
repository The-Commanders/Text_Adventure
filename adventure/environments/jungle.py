import random


class Jungle:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.stamina = 10
        self.description = """You arrive at the jungle, home to wildlife and indigenous tribes. Tread carefully as 
        danger could be around every corner!"""

    def event_one(self):

        print("As you are walking through the jungle, you come across a patch of thick patch of vine blocking your "
              "path.")
        print("There seems to be just enough room to squeeze through, however, there is no way to tell what may be "
              "inside...")

        print("1. Try to squeeze through.")
        print("2. Find another path.")
        print("3. Cut through the vines and clear a path (requires Survival Knife).")

        while True:
            selection = input("Pick 1, 2 or 3\n>")
            if selection == "1":
                rand_stam_loss = random.randint(1, 2)
                self.health -= rand_stam_loss
                print(f" You try squeezing through the vines. After what seems like forever, you finally get through "
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
                print(f"You use you knife to cut through the vines. As you are cutting a snake lands on your shoulder "
                      f"and bites you in the neck. -2 HP")
                break
            else:
                print("Please pick 1, 2, or 3.")

    def event_two(self):
        print("As you are walking through the jungle, you come across a pitfall trap that seems to have been "
              "triggered.")
        print("You peer into the trap to see the remains of a another person who unfortunately triggered the trap...")

        print("1. Jump over the trap.")
        print("2. Find another path.")
        print("3. Safely swing across the trap (requires Rope).")

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
                print(f"With rope in hand, you toss it over a sturdy tree branch and safely swing across. ")
                break
            else:
                print("Please pick 1, 2, or 3.")

    def event_three(self):
        print("You are one step closer to getting out of this dangerous jungle. This difficult journey has taken a "
              "toll on your health and stamina. It hasn't been easy but you are almost there. To demonstrate you are "
              "worth of jumping into the next stage, you must test your wit. So please complete one of the following "
              "challenges to continue.")
        print("1. Guess the country")
        print("2. Solve the riddle.")
        print("3. Rock, Paper, Scissor.")

        while True:
            selection = input("Pick 1, 2 or 3\n>")
            if selection == "1":
                print("If I am in Barcelona...")
                user_input = input("...in which country am I? Enter your answer:")
                if user_input.lower() == "spain":
                    print("Correct! You've recovered some health and stamina")
                    self.health += 1
                    self.stamina += 1
                else:
                    print('Incorrect.')
            elif selection == "2":
                print("What five-letter word becomes shorter when you add two letters to it?.")
                user_input = input("Enter your answer:")
                if user_input.lower() == "short":
                    print("Correct! You've recovered some health and stamina")
                    self.health += 1
                    self.stamina += 1
                else:
                    print("Incorrect.")
            elif selection == "3":
                self.play_rock_paper_scissors()
            break

        print("Your current health is:", self.health)
        print("Your current stamina is:", self.stamina)

    def play_rock_paper_scissors(self):
        print("Welcome to Rock, Paper, Scissors!")
        choices = ["rock", "paper", "scissors"]
        player_score = 0
        monkey_score = 0

        for game_round in range(1, 4):
            print("Round", game_round)
            player_choice = input("You have three rounds to beat the monkey to Rock, Paper, Scissors. "
                                  "Pick 1 for rock, 2 for paper or 3 for scissors\n>")
            if player_choice not in ["1", "2", "3"]:
                print("Invalid input. Please enter a number between 1 and 3.")

            # convert player's choice from a string to an integer and subtract 1 from it.
            player_choice = int(player_choice) - 1
            monkey_choice = random.randint(0, 2)

            print("Player chooses:", choices[player_choice])
            print("Monkey chooses:", choices[monkey_choice])

            result = self.game_winner(player_choice, monkey_choice)

            if result == "player":
                player_score += 1
                print("You win this round!")
            elif result == "monkey":
                monkey_score += 1
                print("Monkey wins this round!")
            else:
                print("It's a tie!")

            print("Player Score:", player_score)
            print("Monkey Score:", monkey_score)

        if player_score > monkey_score:
            print("Congratulations! You've beaten the monkey and recovered stamina and health!")
        elif player_score < monkey_score:
            print("Oops! Seems like the monkey beat you to Rock, Paper, Scissor and, on top of that, you lost some"
                  "stamina.")
        else:
            print("It's a tie!")

    def game_winner(self, player_choice, monkey_choice):
        if player_choice == monkey_choice:
            return None

        if (player_choice == 0 and monkey_choice == 2) or \
                (player_choice == 1 and monkey_choice == 0) or \
                (player_choice == 2 and monkey_choice == 1):
            return "player"
            self.health += 1
            self.stamina += 1
        else:
            return "monkey"
            rand_stam_loss = random.randint(1, 2)
            self.stamina -= rand_stam_loss


if __name__ == "__main__":
    user_choice = Jungle("Jungle")
    user_choice.event_one()
    user_choice.event_two()
    user_choice.event_three()


