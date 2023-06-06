import pytest
import random
from rich.console import Console
from rich.prompt import Prompt
from adventure.environments.ruins_entrance import RuinsEntrance
from adventure.confirm_evironment import confirm_environment

console = Console()


def test_ruins_entrance_exists():

    ruins_entrance = RuinsEntrance(console.print, Prompt.ask)

    assert ruins_entrance


def test_ruins_ent_event_one_c1():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock with your survival knife
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 1
[#FFA500]
    You managed to enter the ruins, but at a great expense. You are drained of stamina.
    """

    sim_choice = ["1"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_one_c2():
    expected_text = """
  [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock with your survival knife
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 2
[#FFA500]
    Did you really think you would be able to pick the lock? You've made a great effort but
    accomplished nothing.

        """

    sim_choice = ["2"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_one_c3():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    It seems like the door to get into the ruins is closed and you don't have the key. How would you like
    to proceed in order to gain access to the ruins?
    1. Climb the wall using your grappling hook.
    2. Try and pick the lock with your survival knife
    3. Try and find the key somewhere around.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:
: 3
[#FFA500]
    That was a long and unsuccessful walk. The key is nowhere to be found, just like your energy.

        """

    sim_choice = ["3"]

    confirm_environment(RuinsEntrance, "event_one", expected_text, sim_choice)


def test_ruins_ent_event_two_c1():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 1
[#FFA500]
    There are way too many to kill them all and they are attacking you.


     """

    sim_choice = ["1"]

    confirm_environment(RuinsEntrance, "event_two", expected_text, sim_choice)


def test_ruins_ent_event_two_c2():
    expected_text = """
 [#FFA500]
    Congratulations, you've made it to the ruins. You are one step closer to getting the idol. However, in 
    order to get your hands on it you will have to test your strength and wit a few more times.
    
    As you jump into the ruins, you find yourself surrounded by scorpions. 
        What do you do?
    "1. Try to kill them with your survival knife.
    "2. Run as fast as you can into the ruins so they don't catch you.
    "3. Climb the wall back out.
[#FFA500]
    Enter your choice(1, 2, 3), enter 'i' to use an item:  
    : 2
[#FFA500]
    You are one fast runner! You've made it without loosing any health.

     """

    sim_choice = ["2"]

    confirm_environment(RuinsEntrance, "event_two", expected_text, sim_choice)