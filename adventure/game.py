# acts as our Node
import random


class Environment:

    def __init__(self, data, next=None):
        self.data = data
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
        """
        Lists the environments out in a string format
        :return: A list of environments
        """
        current = self.head
        ll_list = []
        while current is not None:
            ll_list.append(str(current.data.name))
            current = current.next
        return " -> ".join(["{ " + value + " }" for value in ll_list] + ["None"])

    # serves as our traverse method
    def traverse_environments(self):
        if not self.head:
            return "There is no head"

        current = self.head

        while current:
            self.trigger_event(current)
            current = current.next

    def trigger_event(self, current=None):
        """
        Triggers a random event to occur in the current environment
        :param current: The current environment
        :return: current environments randomly chosen event
        """
        # event_list = current.data.func
        # event_list[random.randint(0, len(event_list) - 1)]()
        # event_list()

    # serves as our insert method
    def add_environment(self, data):
        """
        adds an environment
        :param data: The instance environment
        :return:
        """
        new_node = Environment(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node





