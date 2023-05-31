from rich.console import Console
import random
from rich.style import Style


def reward_room():
    console = Console()
    reward_style = Style(color="#1F51FF", bold=True)
    console.print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |                                                                                      |
     |               You been blessed with luck! You've found a reward room!                |
     \                                                                                      /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """, style=reward_style)

    rand = random.randint(1, 3)

    # game_logic = GameLogic()
    # random_item = random.sample(game_logic.items, 1)

    if rand == 1:
        console.print(f"""
        You walk into the mysterious room, not sure what to expect.
        The room is nicely decorated with many different cave paintings,
        perhaps describing the culture of the people who live in the
        jungle? In the center of the room stands an offering bowl.
        You peer inside to find a [i #1F51FF]item[/i #1F51FF] inside! Just your luck. 
    
    """, style=reward_style)

    elif rand == 2:
        console.print("""
        You walk into the mysterious room, not sure what to expect.
        Upon entering, you see a gorgeous fountain shooting 
    """, style=reward_style)

    elif rand == 3:
        console.print("""
        restore stamina
    """, style=reward_style)


if __name__ == "__main__":
    reward_room()
