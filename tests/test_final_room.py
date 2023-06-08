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
    Stepping into the final room ready to face your final challenge, you notice somethings off. The idol stands
    before you. Proceeding carefully, you grab the idol on the desk before you. Examining the idol before you,
    you notice writing on the base reading "[i yellow]MADE IN CHINA[/i yellow]". Of course it wouldn't be this
    easy, the floor caves in from below you, you must think quickly!
        What do you do?
    1. Leap of faith
    2. Grab the side ledge
    3. Jump over the ledge, find a new way through
    
[purple]
    Enter your choice(1, 2, 3) 
    : 1
[purple]
    Your first reaction is to trust the fall, weird but ok? You fall for a few seconds,
    expecting to break a bone or 2, but somehow you land in a convenient hay stack. Thats
    just what you needed! Not the smartest decision, as you take -2 [red]health[/red] and [yellow]stamina[/yellow].
    You continue on to the idols room.
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
    Stepping into the final room ready to face your final challenge, you notice somethings off. The idol stands
    before you. Proceeding carefully, you grab the idol on the desk before you. Examining the idol before you,
    you notice writing on the base reading "[i yellow]MADE IN CHINA[/i yellow]". Of course it wouldn't be this
    easy, the floor caves in from below you, you must think quickly!
        What do you do?
    1. Leap of faith
    2. Grab the side ledge
    3. Jump over the ledge, find a new way through
    
[purple]
    Enter your choice(1, 2, 3) 
    : 2
[purple]
    Quickly thinking, you grab the side ledge before falling into the abyss. That was way too
    close! Your quick save costed -2 [yellow]stamina[/yellow], but better than breaking a leg
    in an ancient temple. You continue on to the idol room.
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
    Stepping into the final room ready to face your final challenge, you notice somethings off. The idol stands
    before you. Proceeding carefully, you grab the idol on the desk before you. Examining the idol before you,
    you notice writing on the base reading "[i yellow]MADE IN CHINA[/i yellow]". Of course it wouldn't be this
    easy, the floor caves in from below you, you must think quickly!
        What do you do?
    1. Leap of faith
    2. Grab the side ledge
    3. Jump over the ledge, find a new way through
    
[purple]
    Enter your choice(1, 2, 3) 
    : 3
[purple]
    Mustering up all your strength, you make the jump too the opposite side, loosing your footing
    for a second, you catch yourself. With a brief sigh of relief, and continue your search for a
    MUCH safer route downwards.

        """
    simulated_choice = ["3"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_one", expected_text, simulated_choice)


def test_final_room_event_two_c1():
    expected_text = """
[purple]
    Stepping into the final room, you feel uneasy. Its just a regular room, nothing special. You feel the ground
    starting to shake underneath you and rocks start to form into the shape of a figure, creating a huge guardian.
    The guardian turns to you with its eyes flashing [red]red[/red], not good! 
    What do you do?
    1. Create a rope trap using your rope and escape
    2. Stealth approach and use your survival knife to attack.
    3. Distract and strike with rocks.
    

    Enter your choice(1, 2, 3): 
    : 1
[purple]
    You successfully set up the rope trap and, as expected, the guardian starts to move forward. The 
    guardian's foot catches the snare, causing it to stumble and lose balance. Seizing this opportunity, 
    you escape the room but you cut your shoulder on the way out, -2 [red]health[/red].
            """
    simulated_choice = ["1"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_two_c2():
    expected_text = """
      [purple]
    Stepping into the final room, you feel uneasy. Its just a regular room, nothing special. You feel the ground
    starting to shake underneath you and rocks start to form into the shape of a figure, creating a huge guardian.
    The guardian turns to you with its eyes flashing [red]red[/red], not good! 
    What do you do?
    1. Create a rope trap using your rope and escape
    2. Stealth approach and use your survival knife to attack.
    3. Distract and strike with rocks.
    

    Enter your choice(1, 2, 3): 
    : 2

    [purple]You do not have a [#1F51FF]survival knife[/#1F51FF]!

    Enter your choice(1, 2, 3): 
    : 1
[purple]
    You successfully set up the rope trap and, as expected, the guardian starts to move forward. The 
    guardian's foot catches the snare, causing it to stumble and lose balance. Seizing this opportunity, 
    you escape the room but you cut your shoulder on the way out, -2 [red]health[/red].
            """
    simulated_choice = ["2", "1"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_two_c3():
    expected_text = """
  [purple]
    Stepping into the final room, you feel uneasy. Its just a regular room, nothing special. You feel the ground
    starting to shake underneath you and rocks start to form into the shape of a figure, creating a huge guardian.
    The guardian turns to you with its eyes flashing [red]red[/red], not good! 
    What do you do?
    1. Create a rope trap using your rope and escape
    2. Stealth approach and use your survival knife to attack.
    3. Distract and strike with rocks.
    

    Enter your choice(1, 2, 3): 
    : 3
[purple]
    You pick a small stone from the ground and hurl it to a corner of the room, away from your intended 
    path. The guardian, being vigilant, turns its head toward the sound and moves away from its original 
    position, temporarily distracted by the false threat. You take advantage of this opportunity to move 
    swiftly and silently towards the guardian. You strike various powerful attacks to the guardian's weak spot with 
    rocks you pick from the ground. The guardian lets out a roar of pain and dies.
            """
    simulated_choice = ["3"]
    random_int = []

    confirm_environment(RuinsFinalRoom, "event_two", expected_text, simulated_choice)


def test_final_room_event_three_c1():
    expected_text = """
 [purple]
    As you step into the final room, you hear a voice echoing throughout the room. "Hello adventurer, let's see if  
    you are worthy, step forward and pick a challenge".
    You step forward and read on the wall...
    1. Guess the number.
    2. Play hangman.
    

    Enter your choice(1, 2)
    : 1
[purple]
    Welcome to Guess the Number!
    
Guess a number between 1 and 100. You have 8 attempts:: 25
[purple]
    The number you've entered is too low!
    
Guess a number between 1 and 100. You have 7 attempts:: 75
[purple]
    The number you've entered is too high!
    
Guess a number between 1 and 100. You have 6 attempts:: 50
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

