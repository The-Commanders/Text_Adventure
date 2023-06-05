# acts as our Node
import random
from rich.console import Console

console = Console()



class Environment:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Game Logic class
class GameLogic:
    def __init__(self, starting_item):
        self.head = None
        self.health = 10
        self.stamina = 10
        self.inventory = [starting_item, "med spray", "ration"]
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
        while current is not None:
            console.print(f"[green] The current environment is: {str(current.data.name)} [/green]")
            self.add_resources(current)
            print("Current Health: ", current.data.health)
            print("Current Stamina: ", current.data.stamina)
            print("Current Items: ", " ".join(current.data.inventory))
            self.trigger_random_event(current.data)
            self.update_resources(current)
            current = current.next
        return "Traversal completed successfully"

    def trigger_random_event(self, data=None):
        """
        Triggers a random event to occur in the current environment
        :param data: The current environment
        :return: current environments randomly chosen event
        """
        current_node = data
        event_names = [name for name in dir(current_node) if callable(getattr(current_node, name)) and not name.startswith("__") and "event" in name]
        # print(event_names)
        random_event_name = random.choice(event_names)
        # print(random_event_name)
        random_event = getattr(current_node, random_event_name)
        random_event()

    # serves as our insert method
    def add_environment(self, data=None):
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

    def update_resources(self, data=None):
        """
        Updates the players resources after every environment
        :param data:
        :return: none
        """
        current_node = data

        self.health = current_node.data.health
        self.stamina = current_node.data.stamina
        self.inventory = current_node.data.inventory

    def add_resources(self, current_node):
        """
        Adds the resources in game logic into the current environment
        :param current_node: the current environment
        :return: none
        """
        current_node.data.health = self.health
        current_node.data.stamina = self.stamina
        current_node.data.inventory = self.inventory




