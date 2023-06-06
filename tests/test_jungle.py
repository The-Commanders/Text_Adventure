import pytest
from adventure.environments.jungle import Jungle
from adventure.confirm_evironment import *
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


def test_jungle_event_one_c2():
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
    [/green]: 2
[green]
    In your search for another path, you end up stepping on a monkey trap. You free yourself and
    step on another trap. This continues for roughly an hour until you finally find a clear path..
    -[red]2 HP[/red]!

        """
    simulated_choice = ["2"]
    random_ints = [2]

    confirm_environment(Jungle, "event_one", expected_text, simulated_choice, random_ints)
    pass


def test_jungle_event_one_c3_with_sknife():
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
    [/green]: 3
[green]
    You use you knife to cut through the vines. As you are cutting a snake lands on your shoulder
    and bites you in the neck. -2 [red]HP[/red]
    """

    simulated_choice = ["3"]
    # random_ints = [1]

    confirm_environment(Jungle, "event_one", expected_text, simulated_choice)


def test_jungle_event_one_c3_without_sknife():
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
    [/green]: 3
[green]
    You do not have a [#9D00FF]survival knife[/#9D00FF] in your inventory!
    
[green]
    Pick 1, 2 or 3 or 'i' to use an item
    [/green]: 1
[green] 
    You try squeezing through the vines. After what seems like forever, you finally get through
    the vines and continue on your path. -[yellow]1 stamina[/yellow]!
    """

    simulated_choice = ["3", "1"]
    random_ints = [1]

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
Items List:1. med spray2. ration
Please select an item you would like to use: ration
You recovered 5 SP!
[green]
    Pick 1, 2 or 3 or 'i' to use an item
    [/green]: 1
[green] 
    You try squeezing through the vines. After what seems like forever, you finally get through
    the vines and continue on your path. -[yellow]4 stamina[/yellow]!

        """

    simulated_choice = ["i", "ration", '1']
    random_ints = [4]

    confirm_environment(Jungle, "event_one", expected_text, simulated_choice, random_ints)


def test_jungle_event_two_c1():
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
    : 1
[green]
    You have a bad running start and as a result, you barely clear the gap
    and injure yourself a little. -[yellow]1 stamina[/yellow], -[red]2 HP[/red]! 

    """

    simulated_choice = ["1"]
    random_ints = [1, 2]

    confirm_environment(Jungle, "event_two", expected_text, simulated_choice, random_ints)


def test_jungle_event_two_c2():
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
    """

    simulated_choice = ["2"]
    random_ints = [5]

    confirm_environment(Jungle, "event_two", expected_text, simulated_choice, random_ints)


def test_jungle_event_two_c3():
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
    : 3
[green]
    With rope in hand, you toss it over a sturdy tree branch and safely swing across. -[yellow]2 stamina[/yellow]
    """

    sim_choice = ["3"]
    random_ints = [2]

    confirm_environment(Jungle, "event_two", expected_text, sim_choice, random_ints)


def test_jungle_event_four_c1():
    expected_text = """
     [green]
    You come across a monkey while on your journey.
    The monkey looks as if it has been entangled by the tree vines!

    1. Untangle the monkey
    2. Leave the monkey there and make fun of it
    3. Ignore the monkey and continue on your journey

[green]
    Pick 1, 2 or 3
    : 1
[green]
    The monkey runs and climbs up a tree and brings you a banana! +[yellow]1[/yellow] stamina!

    """
    sim_choice = ["1"]
    random_ints = [1]
    confirm_environment(Jungle, "event_four", expected_text, sim_choice, random_ints)

def test_jungle_event_four_c2():
    expected_text = """
 [green]
    You come across a monkey while on your journey.
    The monkey looks as if it has been entangled by the tree vines!

    1. Untangle the monkey
    2. Leave the monkey there and make fun of it
    3. Ignore the monkey and continue on your journey
    
[green]
    Pick 1, 2 or 3
    : 2
[green]
    The monkey gets angry, and  manages to free itself! It grabs a rock nearby and throws it at you!"
    -[red]3 HP[/red]!


    """
    sim_choice = ["2"]
    random_ints = [3]
    confirm_environment(Jungle, "event_four", expected_text, sim_choice, random_ints)

def test_jungle_event_four_c3():
    expected_text = """
 [green]
    You come across a monkey while on your journey.
    The monkey looks as if it has been entangled by the tree vines!

    1. Untangle the monkey
    2. Leave the monkey there and make fun of it
    3. Ignore the monkey and continue on your journey
    
[green]
    Pick 1, 2 or 3
    : 3
[green]
    You begin to walk away. As you are walking you hear the monkey screech!
    You run back to check the commotion, and you the see monkey being devoured by an anaconda.
    It is very traumatizing... -[red]1 HP[/red], -[yellow]1 stamina[/yellow]!

    """
    sim_choice = ["3"]
    # random_ints = []
    confirm_environment(Jungle, "event_four", expected_text, sim_choice)


