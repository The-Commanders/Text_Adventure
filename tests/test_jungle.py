import pytest
# from adventure.game import InvalidDataTypeError
from adventure.environments.jungle import Jungle
from adventure.confirm_evironment import confirm_environment
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def test_jungle_exists():

    jungle = Jungle(console.print, Prompt.ask)
    # actual = jungle.name
    # expected = "jungle"

    assert jungle

def test_jungle_event_one_c1():
    expected_text = """
     [green]
    As you are walking through the jungle, you come across a patch of thick vines 
    blocking your path. There seems to be just enough room to squeeze through, however, 
    there is no way to tell what may be inside...
    1. Try to squeeze through
    2. Find another path
    3. Cut through the vines and clear a path (requires [#9D00FF]Survival Knife[/#9D00FF])
    [/green]
[green]
    Pick 1, 2 or 3 or 'i' to use an item
    [/green]: 1
[green] 
    You try squeezing through the vines. After what seems like forever, you finally get through
    the vines and continue on your path. -[yellow]4 stamina[/yellow]!
    """

    simulated_choice = ["1"]
    random_ints = [4]

    confirm_environment(Jungle, "event_one", expected_text, simulated_choice, random_ints)


def test_jungle_event_one_use_item_c1():
    expected_text = """
         [green]
        As you are walking through the jungle, you come across a patch of thick vines 
        blocking your path. There seems to be just enough room to squeeze through, however, 
        there is no way to tell what may be inside...
        1. Try to squeeze through
        2. Find another path
        3. Cut through the vines and clear a path (requires [#9D00FF]Survival Knife[/#9D00FF])
        [/green]
    [green]
        Pick 1, 2 or 3 or 'i' to use an item
        [/green]: i
    [green] 
        You try squeezing through the vines. After what seems like forever, you finally get through
        the vines and continue on your path. -[yellow]4 stamina[/yellow]!
        """

    simulated_choice = ["i"]
    random_ints = [4]

    confirm_environment(Jungle, "event_one", expected_text, simulated_choice, random_ints)


def test_jungle_event_one_c2():
    expected_text = """
 [green]
    As you are walking through the jungle, you come across a pitfall trap that seems 
    to have been triggered. You peer into the trap to see the remains of a another person 
    who unfortunately triggered the trap...

    1. Jump over the trap
    2. Find another path
    3. Safely swing across the trap ([#9D00FF]requires Rope[/#9D00FF])
    
[green]
    Pick 1, 2 or 3 or 'i' to use an item.
    : 2
[green]
    In your search for another path, you end up stepping on a monkey trap.
    You free yourself and step on another trap. This continues for roughly 
    an hour until you finally find a clear path.. -[red]5 HP[/red]!
    [green]Health: 3[/green]
[yellow]Stamina: 5[/yellow]
[white]Inventory: med spray, ration[/white]

    """

    simulated_choice = ["2"]
    random_ints = [5]

    confirm_environment(Jungle, "event_two", expected_text, simulated_choice, random_ints)