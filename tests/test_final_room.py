import pytest
from rich.console import Console
from rich.prompt import Prompt
from adventure.confirm_evironment import confirm_environment
from adventure.environments.ruins_final_room import RuinsFinalRoom

console = Console()

def test_final_room_exists():
    final_room = RuinsFinalRoom(console.print, Prompt.ask)
    assert final_room

def test_final_room_event_one_c1():
    expected_text = """
     [bold purple]
    Congratulations for making it to the final room. You've displayed great strength and wit across 
    all stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?
    [purple]
    As you venture into the ruins you see the idol in the middle of the room. It's been carefully placed on the 
    floor right in the center. Something is off. You can feel it in your gut. You start walking very slowly towards the 
    idol, uncertain of what might happen once you get your hands on it. As you start walking towards the center of the 
    room the floor starts shaking. What is happening?? The ground starts to collapse taking the idol with it into the 
    depths. What do you do?
    [yellow]1. Swing to safety.[green]2. Descend to a lower level.[blue]3. Create a bridge.

    Enter your choice(1, 2, 3) 
    : 1
[purple]
    You throw your grappling hook into a sturdy structure above. The hook catches onto the surface and 
    you leap off the collapsing ground and swing across the room to stable ground. [yellow]-2 stamina[/yellow]
    """
    simulated_choice = ["1"]
    # random_int = []

    confirm_environment(RuinsFinalRoom, "event_one", expected_text, simulated_choice)
def test_final_room_event_one_c2():
    expected_text = """
     [bold purple]
    Congratulations for making it to the final room. You've displayed great strength and wit across 
    all stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?
    [purple]
    As you venture into the ruins you see the idol in the middle of the room. It's been carefully placed on the 
    floor right in the center. Something is off. You can feel it in your gut. You start walking very slowly towards the 
    idol, uncertain of what might happen once you get your hands on it. As you start walking towards the center of the 
    room the floor starts shaking. What is happening?? The ground starts to collapse taking the idol with it into the 
    depths. What do you do?
    [yellow]1. Swing to safety.[green]2. Descend to a lower level.[blue]3. Create a bridge.

    Enter your choice(1, 2, 3) 
    : 2
[purple]
    You notice a lower level below, so you quickly attach your grappling hook to a secure structure and 
    start rappelling down using the rope. Carefully descending, you land safely on the lower level.
        """
    simulated_choice = ["2"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_one", expected_text, simulated_choice)
def test_final_room_event_one_c3():
    expected_text = """
     [bold purple]
    Congratulations for making it to the final room. You've displayed great strength and wit across 
    all stages of the game but getting your hands on the idol won't be an easy endeavor. Are you ready?
    [purple]
    As you venture into the ruins you see the idol in the middle of the room. It's been carefully placed on the 
    floor right in the center. Something is off. You can feel it in your gut. You start walking very slowly towards the 
    idol, uncertain of what might happen once you get your hands on it. As you start walking towards the center of the 
    room the floor starts shaking. What is happening?? The ground starts to collapse taking the idol with it into the 
    depths. What do you do?
    [yellow]1. Swing to safety.[green]2. Descend to a lower level.[blue]3. Create a bridge.

    Enter your choice(1, 2, 3) 
    : 3
[purple]
    You see there are still some stable sections of ground on some sides of the chasm, so you use your 
    grappling hook and rope to create a makeshift bridge. You secure the end of the rope to a study 
    structure and throw the grappling hook to stable round on the opposite side. Once your hook catches 
    onto the ground, you tighten the create and create a stable bridge. You carefully walk across.
        """
    simulated_choice = ["3"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_one", expected_text, simulated_choice)


def test_final_room_event_two_c1():
    expected_text = """
     [purple]
    Suddenly a cloud of smoke and dust covers everything, making it impossible to see what's happening around you. 
    When the dust settles you see it, it's the ancient guardian of the ruins. You had heard about it before, but 
    always thought it was just a myth. It seems like you will have to beat it to get the idol. What do you do?
    [yellow]1. Create a rope trap using your grappling hook, rope and knife.[green]2. Stealth approach and use your survival knife to attack.[blue]3. Distract and strike with your survival knife.

    Enter your choice(1, 2, 3): 
    : 1
[purple]
    You successfully set up the rope trap and, as expected, the guardian starts to move forward. The 
    guardian's foot catches the snare, causing it to stumble and lose balance. Seizing this opportunity, 
    you rush forward and attack the vulnerable area on the guardian's back with your survival knife. The 
    guardian lets out a roar of pain and temporarily loses focus, giving you 
    a chance to deal further damage.
            """
    simulated_choice = ["1"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_two_c2():
    expected_text = """
     [purple]
    Suddenly a cloud of smoke and dust covers everything, making it impossible to see what's happening around you. 
    When the dust settles you see it, it's the ancient guardian of the ruins. You had heard about it before, but 
    always thought it was just a myth. It seems like you will have to beat it to get the idol. What do you do?
    [yellow]1. Create a rope trap using your grappling hook, rope and knife.[green]2. Stealth approach and use your survival knife to attack.[blue]3. Distract and strike with your survival knife.

    Enter your choice(1, 2, 3): 
    : 2
[purple]
    You successfully reach a position near the guardian's vulnerable spot without being detected. You 
    unleash a swift and precise attack, driving your survival knife into the weak area. The guardian lets 
    out a roar of pain, but it remains standing. Realizing that you have a limited window of opportunity, 
    you must act quickly and retreat to cover before the guardian retaliates. You return to the shadows, 
    evading the guardian's gaze and avoiding its powerful attacks.

            """
    simulated_choice = ["2"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_two_c3():
    expected_text = """
 [purple]
    Suddenly a cloud of smoke and dust covers everything, making it impossible to see what's happening around you. 
    When the dust settles you see it, it's the ancient guardian of the ruins. You had heard about it before, but 
    always thought it was just a myth. It seems like you will have to beat it to get the idol. What do you do?
    [yellow]1. Create a rope trap using your grappling hook, rope and knife.[green]2. Stealth approach and use your survival knife to attack.[blue]3. Distract and strike with your survival knife.

    Enter your choice(1, 2, 3): 
    : 3
[purple]
    You pick a small stone from the ground and hurl it to a corner of the room, away from your intended 
    path. The guardian, being vigilant, turns its head toward the sound and moves away from its original 
    position, temporarily distracted by the false threat. You take advantage of this opportunity to move 
    swiftly and silently towards the guardian. With your survival knife you strike a powerful attack to the 
    guardian's weak spot. The guardian lets out a roar of pain and dies.

            """
    simulated_choice = ["3"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_three_c1():
    expected_text = """
     [purple]
    As the echoes of battle subside, the ruins' atmosphere takes on an eerie calmness. Your gaze shifts towards the 
    center of the final room, where a magnificent pedestal starts to rise from the ground. It is mesmerizing. 
    Adorned with ancient inscriptions and symbols. It becomes clear that the last obstacle standing between you and 
    the idol is an intricate puzzle, requiring both intellect and intuition to unravel. Complete the following two 
    challenges to obtain the idol.
    [yellow]1. Guess the number.[green]2. Play hangman.

    Enter your choice(1, 2)
    : 1
[purple]
    Welcome to Guess the Number!
    
Guess a number between 1 and 100. You have 8 attempts:: 25
[purple]
    The number you've entered is too low!
    
Guess a number between 1 and 100. You have 8 attempts:: 75
[purple]
    The number you've entered is too high!
    
Guess a number between 1 and 100. You have 8 attempts:: 50
[purple]
    Congratulations! You've guessed the number!
    """
    simulated_choice = ["1", "25", "75", "50"]
    random_int = [50]

    confirm_environment(RuinsFinalRoom, "event_three", expected_text, simulated_choice, random_int)


@pytest.mark.skip
def test_final_room_event_three_c2():
    expected_text = """

    """
    simulated_choice = ["2", "a", "e", "i", "o", "u"]
    random_int = [50]

    confirm_environment(RuinsFinalRoom, "event_three", expected_text, simulated_choice)

