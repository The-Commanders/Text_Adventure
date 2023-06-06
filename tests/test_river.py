import pytest
from rich.console import Console
from rich.prompt import Prompt
from adventure.environments.river import River
from adventure.confirm_evironment import confirm_environment

console = Console()


def test_river_exists():
    river = River(console.print, Prompt.ask)
    assert river


def test_river_event_one_c1():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The base of the river seems to have no simple way across, just your luck!
    How will you get across, looks like there are a few ways..
    1. Swim across the river
    2. Build a makeshift raft and sail across
    3. Look for a bridge upstream.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 1
[cyan]
    You swim across the river. It was tiring, and you lost [yellow]]3 stamina[/yellow].
    """

    simulated_choice = ["1"]
    random_int = [3]

    confirm_environment(River, "event_one", expected_text,simulated_choice, random_int)


def test_river_event_one_c2():
    expected_text = """
     [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The base of the river seems to have no simple way across, just your luck!
    How will you get across, looks like there are a few ways..
    1. Swim across the river
    2. Build a makeshift raft and sail across
    3. Look for a bridge upstream.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 2
[cyan]
    You build a makeshift raft and sail across the river. As you sail across, you remember that you have zero experience
    with building a raft. The raft sinks and you are forced to swim the rest of the way. You lost [red]4 
    health[/red] from entire ordeal!
        """

    simulated_choice = ["2"]
    random_int = [4]

    confirm_environment(River, "event_one", expected_text, simulated_choice, random_int)


def test_river_event_one_c3():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The base of the river seems to have no simple way across, just your luck!
    How will you get across, looks like there are a few ways..
    1. Swim across the river
    2. Build a makeshift raft and sail across
    3. Look for a bridge upstream.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item: 
    : 3
[cyan]
    You find a bridge upstream and cross the river [green]safely[/green].
        """

    simulated_choice = ["3"]

    confirm_environment(River, "event_one", expected_text, simulated_choice)


def test_river_event_two_c1():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    As you traverse the riverside looking for a way across, you encounter a dangerous
    crocodile, and he looks hungry!
        What do you do?
    1. Fight the creature.
    2. Try to evade the danger.
    3. Stand your ground.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: 1
[cyan]
    You take on the croc Happy Gilmore style. Except, this is anything at all like the movie! Instead you are badly 
    injured by the crocodile! You lost [red]6 HP[/red].
    """

    simulated_choice = ["1"]
    random_int = [6]

    confirm_environment(River, "event_two", expected_text, simulated_choice, random_int)


def test_river_event_two_3invalid_choices_into_c1():
    expected_text = """
  [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    As you traverse the riverside looking for a way across, you encounter a dangerous
    crocodile, and he looks hungry!
        What do you do?
    1. Fight the creature.
    2. Try to evade the danger.
    3. Stand your ground.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: one
[cyan]
    [red]Invalid choice![/red]
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: two
[cyan]
    [red]Invalid choice![/red]
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: three
[cyan]
    [red]Invalid choice![/red]
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: 1
[cyan]
    You take on the croc Happy Gilmore style. Except, this is anything at all like the movie! Instead you are badly 
    injured by the crocodile! You lost [red]6 HP[/red].
    """

    simulated_choice = ["one", "two", "three", "1"]
    random_int = [6]

    confirm_environment(River, "event_two", expected_text, simulated_choice, random_int)


def test_river_event_two_c2():
    expected_text = """
     [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    As you traverse the riverside looking for a way across, you encounter a dangerous
    crocodile, and he looks hungry!
        What do you do?
    1. Fight the creature.
    2. Try to evade the danger.
    3. Stand your ground.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: 2
[cyan]
    You manage to evade the danger, but it tires you out -1 stamina!
    """
    simulated_choice = ["2"]
    random_int = [1]

    confirm_environment(River, "event_two", expected_text, simulated_choice, random_int)


def test_river_event_two_c3():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    As you traverse the riverside looking for a way across, you encounter a dangerous
    crocodile, and he looks hungry!
        What do you do?
    1. Fight the creature.
    2. Try to evade the danger.
    3. Stand your ground.
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item
    Input: 3
[cyan]
    You stand your ground and face the creature. Bad idea! The crocodile attacks and you are forced to flee! 
    It takes a toll on your stamina! [yellow]-2 stamina[/yellow].
        """
    simulated_choice = ["3"]
    random_int = [2]

    confirm_environment(River, "event_two", expected_text, simulated_choice, random_int)


def test_river_event_three_c1_incorrect():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 1
    [cyan]Riddle:[cyan]
    I speak without a mouth and hear without ears. I have no body, 
    but I come alive with wind. What am I?
    
   [cyan]Enter your answer: : sound

    Oops! Your answer is [red]incorrect[/red], and it has taken a toll on your health. [red]-2 HP[/red]!
        """
    simulated_choice = ["1", "sound"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)


def test_river_event_three_c1_correct():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 1
    [cyan]Riddle:[cyan]
    I speak without a mouth and hear without ears. I have no body, 
    but I come alive with wind. What am I?
    
   [cyan]Enter your answer: : echo
[cyan]
    [green]Congratulations[/green]! You solved the riddle and gained [red]2 health[/red].
        """
    simulated_choice = ["1", "echo"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)


def test_river_event_two_c2_correct():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 2

[cyan]
    Type the word '[#9D00FF]challenge[/#9D00FF]' as fast as you can: 
    challenge: challenge

    Well done! You completed the typing challenge and gained some 
    [yellow]stamina[/yellow].

        """
    simulated_choice = ["2", "challenge"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)


def test_river_event_three_c2_incorrect():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 2

[cyan]
    Type the word '[#9D00FF]challenge[/#9D00FF]' as fast as you can: 
    challenge: chalenge
[cyan]
    Oops! Your answer is [red]incorrect[/red], and it has taken 
    a toll on your [yellow]stamina[/yellow].

        """
    simulated_choice = ["2", "chalenge"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)

def test_river_event_three_c3_correct():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 3

[cyan]
    Guess the correct word: It starts with a '[green]S[/green]' and ends with a '[green]t[/green]': 
    Input: secret
[cyan]
    [green]Congratulations[/green]! You guessed the correct word!
            """
    simulated_choice = ["3", "secret"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)

def test_river_event_three_c3_failed():
    expected_text = """
 [cyan]
    You've come across the river, peaceful and calm, but anything could be 
    hiding inside the waters, stay on your toes!
    [cyan]
    The riverside is full of surprises, you come across a suspicious wall, with some prompts
    written on the walls. 'Choose one', reads the wall. Reluctantly, you decide to..
    1. Solve a riddle
    2. Complete a typing challenge
    3. Guess the correct word
    
[cyan]
    Enter your choice (1-3), enter 'i' to use an item:
    : 3

[cyan]
    Guess the correct word: It starts with a '[green]S[/green]' and ends with a '[green]t[/green]': 
    Input: start
[white]
    [red]Incorrect[/red] guess. Try again!
    [white]
    You have 2 attempts left.
    
[cyan]
    Guess the correct word: It starts with a '[green]S[/green]' and ends with a '[green]t[/green]': 
    Input: strat
[white]
    [red]Incorrect[/red] guess. Try again!
    [white]
    You have 1 attempts left.
    
[cyan]
    Guess the correct word: It starts with a '[green]S[/green]' and ends with a '[green]t[/green]': 
    Input: short
[white]
    [red]Incorrect[/red] guess. Try again!
    
    You [red]failed[/red] to guess the word. No treasure for you!
         """
    simulated_choice = ["3", "start", "strat", "short"]
    random_int = [2]

    confirm_environment(River, "event_three", expected_text, simulated_choice, random_int)

# -------Deiosha's Test Code---------
# @pytest.fixture
# def river():
#     return River(console.print, Prompt.ask)

# def test_display_text(capsys, river):
#     river.display_text("Test message")
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "Test message"

# def test_item_collection(capsys, river):
#     river.item_collection()
#     captured = capsys.readouterr()
#     expected_output = """Items in the game:
# - First aid spray
# - Ration"""
#     assert captured.out.strip() == expected_output

# def test_situation_event_one(monkeypatch, capsys, river):
#     monkeypatch.setattr('builtins.input', lambda _: '1')
#     river.event_one()
#     captured = capsys.readouterr()
#     assert "You swim across the river." in captured.out
#
# def test_danger_event_one(monkeypatch, capsys, river):
#     monkeypatch.setattr('builtins.input', lambda _: '1')
#     river.event_two()
#     captured = capsys.readouterr()
#     assert "You engage in a fierce battle." in captured.out
#
# def test_puzzle_event_one(monkeypatch, capsys, river):
#     monkeypatch.setattr('builtins.input', lambda _: '1')
#     river.event_three()
#     captured = capsys.readouterr()
#     assert "Riddle:" in captured.out

# def test_play_game(monkeypatch, capsys, river):
#     monkeypatch.setattr('builtins.input', lambda _: 'next')
#     river.play_game()
#     captured = capsys.readouterr()
#     assert "You have embarked on the River Challenge!" in captured.out