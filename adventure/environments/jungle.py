from game import *

class Jungle:

    def __init__(self, name):
        self.name = name


    @staticmethod
    def event_one():
        print("You come across a patch of thick vinage blocking your path...")
        decision_one = "Try to get through"
        decision_two = "Find another path"
        decision_three = "Cut through the vine and clear a path"
