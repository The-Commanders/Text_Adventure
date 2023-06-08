from rich.console import Console
from rich.prompt import Prompt
from adventure.confirm_evironment import confirm_environment
from adventure.environments.ruins_halls import Ruins_Halls

console = Console()

def test_ruins_halls_exists():
    halls = Ruins_Halls(console.print, Prompt.ask)
    assert halls

def test_halls_event_one_c1():
    expected_text = """
     [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    Your journey has led you into an old room that appears to hold an
    old artifact, perhaps used by the previous inhabitants? who knows
    what it could be used for.. 
        What do you do?"
    1. Inspect the artifact closely
    2. Leave the artifact alone
    3. Take the artifact with you.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 1
[blue]
    You carefully inspect the artifact and find a hidden compartment. 
    Inside, you discover a valuable gem. This gem is brimming with energy! You gain [yellow]+2 stamina[/yellow]!

    """
    simulated_choice = ["1"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_one",expected_text, simulated_choice, random_int)


def test_halls_event_one_c2():
    expected_text = """
 [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    Your journey has led you into an old room that appears to hold an
    old artifact, perhaps used by the previous inhabitants? who knows
    what it could be used for.. 
        What do you do?"
    1. Inspect the artifact closely
    2. Leave the artifact alone
    3. Take the artifact with you.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 2
[blue]
    You decide to leave the artifact undisturbed and continue your journey.
        """
    simulated_choice = ["2"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_one", expected_text, simulated_choice, random_int)


def test_halls_event_one_c3():
    expected_text = """
 [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    Your journey has led you into an old room that appears to hold an
    old artifact, perhaps used by the previous inhabitants? who knows
    what it could be used for.. 
        What do you do?"
    1. Inspect the artifact closely
    2. Leave the artifact alone
    3. Take the artifact with you.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 3
[blue]
        You decide to take the artifact with you, but picking it up triggers an arrow trap! You maneuver and avoid the
        arrows in a panic! Fortunately you escape unscathed, however, now worn out! [yellow] - 2 stamina[/yellow].
            """
    simulated_choice = ["3"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_one", expected_text, simulated_choice, random_int)


def test_halls_event_two_c1():
    expected_text = """
  [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    As you are walking through the hallways, mesmerised by all the exotic paintings,
    your carelessness has caused you to step on a floor trap! Quick, what will you do??
    1. Try to disarm the trap
    2. Jump over the trap
    3. Go back the way you came
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 1
[blue]
    You attempt to disarm the trap but trigger it instead. 
    You get injured, and your [red]health[/red] decreases.
            """
    simulated_choice = ["1"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_two", expected_text, simulated_choice, random_int)


def test_halls_event_two_c2():
    expected_text = """
[blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    As you are walking through the hallways, mesmerised by all the exotic paintings,
    your carelessness has caused you to step on a floor trap! Quick, what will you do??
    1. Try to disarm the trap
    2. Jump over the trap
    3. Go back the way you came
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 2
[blue]
    You muster all your agility and successfully jump over the trap. 
    Your [yellow]stamina[/yellow] decreases slightly.
            """
    simulated_choice = ["2"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_two", expected_text, simulated_choice, random_int)


def test_halls_event_two_c3():
    expected_text = """
  [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    As you are walking through the hallways, mesmerised by all the exotic paintings,
    your carelessness has caused you to step on a floor trap! Quick, what will you do??
    1. Try to disarm the trap
    2. Jump over the trap
    3. Go back the way you came
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 3
[blue]
    You decide it's best to go back the way you came and avoid the trap altogether. 
    Your [yellow]stamina[/yellow] decreases slightly.
    """

    simulated_choice = ["3"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_two", expected_text, simulated_choice, random_int)


def test_halls_event_three_c1():
    expected_text = """
 [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    You discover an iron door blocking your path, with no easy way around. 
    Quite literally stuck between a rock and a hard place, 
        what do you do?
    1. Look for a key to unlock the door
    2. Attempt to pick the lock
    3. Find an alternative route.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 1
[blue]
    You search the surroundings and find a key hidden nearby. 
    Your [yellow]stamina[/yellow] decreases slightly.


    """

    simulated_choice = ["1"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_three", expected_text, simulated_choice, random_int)


def test_halls_event_three_c2():
    expected_text = """
 [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    You discover an iron door blocking your path, with no easy way around. 
    Quite literally stuck between a rock and a hard place, 
        what do you do?
    1. Look for a key to unlock the door
    2. Attempt to pick the lock
    3. Find an alternative route.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 2
[blue]
    You try to pick the lock but accidentally break your lockpick. 
    In the process, you injure yourself, and your [red]health[/red] decreases.

    """

    simulated_choice = ["2"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_three", expected_text, simulated_choice, random_int)


def test_halls_event_three_c3():
    expected_text = """
   [blue]
    You have made your way to the ruin hallways! These halls hold secrets about the ruins,
    and the idol your looking for, but unfortunately for you, the halls contain alot more
    than the idol. Traps could be around every corner, be careful!
    [blue]
    You discover an iron door blocking your path, with no easy way around. 
    Quite literally stuck between a rock and a hard place, 
        what do you do?
    1. Look for a key to unlock the door
    2. Attempt to pick the lock
    3. Find an alternative route.
    
[blue]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 3
[blue]
    You decide to find an alternative route and discover a hidden passage that 
    leads past the locked door. Your [yellow]stamina[/yellow] decreases slightly.

    """

    simulated_choice = ["3"]
    random_int = [2]

    confirm_environment(Ruins_Halls, "event_three", expected_text, simulated_choice, random_int)