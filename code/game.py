# acts as our Node
class Environment:

    def __init__(self, name, next=None):
        self.name = name
        self.next = next

# Game Logic class
class GameLogic:

    def __init__(self):
        self.head = None
        self.health = 10
        self.stamina = 10
        self.inventory = []
        self.items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]

    def __str__(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.name, end=" -> ")
                current = current.next
            print("None")

    # serves as our traverse method
    def traverse_environments(self):
        pass

    # serves as our insert method
    def add_environment(self, name):
        pass

