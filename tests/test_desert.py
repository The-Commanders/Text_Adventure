import pytest
from adventure.environments.desert import Desert
from adventure.confirm_evironment import *
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def test_desert_exists():

    desert = Desert(console.print, Prompt.ask)
    assert desert


def test_desert_event_one_c1():
    expected_text = """
    [bold yellow]You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.

    [yellow]As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.
        [yellow]What will you do?
    1. Refile your stamina at the Oasis
    2. Ignore it and save your energy for more walking, your here for the treasure
    3. Eat a ration ([i #9D00FF]consumes ration[/i #9D00FF])
     Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 1

    [bold red]Not good, you fell for a mirage![/bold red]
    [yellow]Exhausted, you walk back to the path you were taking.
    This took 5 stamina.
    """

    simulated_choice = ["1"]
    random_ints = [5]

    confirm_environment(Desert, "event_one", expected_text, simulated_choice, random_ints)


def test_desert_event_one_c2():
    expected_text = """
    [bold yellow]You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.

    [yellow]As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.
        [yellow]What will you do?
    1. Refile your stamina at the Oasis
    2. Ignore it and save your energy for more walking, your here for the treasure
    3. Eat a ration ([i #9D00FF]consumes ration[/i #9D00FF])
     Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 2
[yellow]
    You continue on, not sure whether to trust your vision or not.
    The heat is is starting to get to you, but you cant give up now!
    This took 2 stamina.

    """

    simulated_choice = ["2"]
    random_ints = [2]

    confirm_environment(Desert, "event_one", expected_text, simulated_choice, random_ints)


@pytest.mark.skip
def test_desert_event_one_c3_with_ration():
    expected_text = """
    [bold yellow]You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.

    [yellow]As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.
        [yellow]What will you do?
    1. Refile your stamina at the Oasis
    2. Ignore it and save your energy for more walking, your here for the treasure
    3. Eat a ration ([i #9D00FF]consumes ration[/i #9D00FF])
     Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 3
[yellow]
    You consumed a [i #9D00FF]ration[/i #9D00FF], and feel better than ever!
    You continue on through the desert with extra stamina!
    You gained 2 stamina!
    """

    simulated_choice = ["3"]
    random_ints = [2]

    confirm_environment(Desert, "event_one", expected_text, simulated_choice, random_ints)

def test_desert_event_one_c3_without_ration():
    expected_text = """
    [bold yellow]You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.

    [yellow]As you walk through the desert for what seems like hours, you see something in the distance.
    Stopping for a moment, you see its an oasis! Palm trees as far as the eye can see, beautiful
    blue shimmering water, and coconuts filled with delicious juice.
        [yellow]What will you do?
    1. Refile your stamina at the Oasis
    2. Ignore it and save your energy for more walking, your here for the treasure
    3. Eat a ration ([i #9D00FF]consumes ration[/i #9D00FF])
     Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 3

[yellow]
    You do not have a [i #9D00FF]ration[/i #9D00FF] in your inventory. Please type 1 or 2.

[blue]Choice[/blue]: 1

    [bold red]Not good, you fell for a mirage![/bold red]
    [yellow]Exhausted, you walk back to the path you were taking.
    This took 2 stamina.
    """

    simulated_choice = ["3", "1"]
    random_ints = [2]

    confirm_environment(Desert, "event_one", expected_text, simulated_choice, random_ints)

def test_desert_event_two_c1():
    expected_text = """
     [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?
        [yellow]What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires grappling hook[/i #9D00FF])
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 1

                    [yellow]You chose the safe route. As you inch out, the sand starts sinking again!
                    You must act fast! Type the words you see on the screen to dig out![/yellow]
                    [red]Warning: 10 seconds will -2 points of health[/red]
                    

            [b red]dig[/b red]: dig


            [b red]push[/b red]: push


            [b red]dig[/b red]: dig

    [bold yellow]
    Your quick thinking got you out of the quicksand!
    It took you 0 seconds to get out,
    that was close, but you can now continue your journey.

    """

    simulated_choice = ["1", "dig", "push", "dig"]
    random_int = [0]

    confirm_environment(Desert, "event_two", expected_text, simulated_choice, random_int)

def test_desert_event_two_c2():

    expected_text = """
     [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?
        [yellow]What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires grappling hook[/i #9D00FF])
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 2

    [red]Looks like the heat has clouded your judgment as well[/red]
    [yellow]Brute force made the sand envelop you much quicker, resulting in
    you almost suffocating in the process! Better be more careful.
    Your health decreased by 3 points.[/yellow]
    """

    simulated_choice = ["2"]
    random_int = [3]

    confirm_environment(Desert, "event_two", expected_text, simulated_choice, random_int)


@pytest.mark.skip
def test_desert_event_two_c3_with_grap_hook():
    expected_text = """
     [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?
        [yellow]What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires grappling hook[/i #9D00FF])
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 3

[bold yellow]
    Great thinking! Using the grappling hook, you through it over the gap
    hitting a rock and latching on! This saves you from struggling.
    You continue on through the desert
    """

    simulated_choice = ["3"]
    confirm_environment(Desert, "event_two", expected_text, simulated_choice)


def test_desert_event_two_c3_without_grap_hook():
    expected_text = """
 [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    Wandering in the heat has taken a toll on you, and its hard to focus. Suddenly you find yourself
    in a pit of quicksand! You are rapidly sinking with each second, and time is running out!
    Think quick, what will you do?
        [yellow]What will you do?
    1. Dig out slowly, the more you panic the worse it will be
    2. Dig yourself out with brute force
    3. Grapple out of the sand ([i #9D00FF]requires grappling hook[/i #9D00FF])
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 3

[bold yellow]
    You dont have the [i #9D00FF]grappling hook[/i #9D00FF] in your inventory!
    please type 1 or 2.

[blue]Choice[/blue]: 2

    [red]Looks like the heat has clouded your judgment as well[/red]
    [yellow]Brute force made the sand envelop you much quicker, resulting in
    you almost suffocating in the process! Better be more careful.
    Your health decreased by 2 points.[/yellow]
    """

    simulated_choice = ["3", "2"]
    random_int = [2]
    confirm_environment(Desert, "event_two", expected_text, simulated_choice, random_int)


def test_desert_event_three_c1_east():
    expected_text = """
     [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    The desert sky is blue and clear, not a cloud in sight. After taking a second
    to admire the atmosphere and setting, you realise you've completely lost your
    sense of direction! You start to panic but collect your thoughts. What can
    help you remember where you've been? Take a second to collect your thoughts
        [yellow]What will you do?
    1. Use the sky for direction
    2. Book it in one direction
    3. Try to remember your surroundings
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 1


[yellow]
    Ok, you were headed north towards the ruins. The current time is 2:48.
    Using the suns position should get you back on track. Using your shadow 
    as reference, which direction is the sun currently?
                        Type either '[blue]east[/blue]' or '[blue]west[/blue]'
    : east

[yellow]
    [red]Incorrect:[/red]
    The sun sets in the west
    You set off towards the south and realise you are going backwards!
    This costs you 2 stamina for going the wrong way!
    """

    simulated_choice = ["1", "east"]
    random_int = [2]

    confirm_environment(Desert, "event_three", expected_text, simulated_choice, random_int)

def test_desert_event_three_c1_west():
    expected_text = """
 [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    The desert sky is blue and clear, not a cloud in sight. After taking a second
    to admire the atmosphere and setting, you realise you've completely lost your
    sense of direction! You start to panic but collect your thoughts. What can
    help you remember where you've been? Take a second to collect your thoughts
        [yellow]What will you do?
    1. Use the sky for direction
    2. Book it in one direction
    3. Try to remember your surroundings
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 1


[yellow]
    Ok, you were headed north towards the ruins. The current time is 2:48.
    Using the suns position should get you back on track. Using your shadow 
    as reference, which direction is the sun currently?
                        Type either '[blue]east[/blue]' or '[blue]west[/blue]'
    : west

[yellow]
    [green]Correct:[/green]
    The sun sets in the west
    You regain your sense of direction and continue on towards the
    ruins, great thinking!

    """

    simulated_choice = ["1", "west"]
    # random_int = [2]

    confirm_environment(Desert, "event_three", expected_text, simulated_choice)


def test_desert_event_three_c3():
    expected_text = """
     [yellow]
    You arrive at the desert, the brutal heat hits you as you feel sweat run down your face.
[yellow]
    The desert sky is blue and clear, not a cloud in sight. After taking a second
    to admire the atmosphere and setting, you realise you've completely lost your
    sense of direction! You start to panic but collect your thoughts. What can
    help you remember where you've been? Take a second to collect your thoughts
        [yellow]What will you do?
    1. Use the sky for direction
    2. Book it in one direction
    3. Try to remember your surroundings
    Choose 1, 2, or 3 or enter "i" to use an item
[blue]Choice[/blue]: 3

[yellow]
    You remember seeing a few objects that can help you remember your direction.
    Unscramble the words to remember the objects you have seen to find the right
    direction to go!
        "lamp erte" "krco" "midrapy" "copsionr"


                            [b red]unscramble[/b red]: palm tree
[green]
                            Correct

                            [b red]unscramble[/b red]: rock
[green]
                            Correct

                            [b red]unscramble[/b red]: pyramid
[green]
                            Correct

                            [b red]unscramble[/b red]: scorpion
[green]
                            Correct
[bold yellow]
    Great work! You remembered the objects!
    As you continue walking, You see the palm tree you passed in the distance,
    you must be going the right way! You continue your journey
    """
    simulated_choice = ["3", "palm tree", "rock", "pyramid", "scorpion"]

    confirm_environment(Desert, "event_three", expected_text, simulated_choice)
