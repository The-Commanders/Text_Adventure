from rich.console import Console
import random
from rich.style import Style


def reward_room(inventory, health, stamina):
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
    items = ["survival knife", "grappling hook", "rope", "med spray", "ration"]
    random_granted_item = random.choice(items)
    # game_logic = GameLogic()
    # random_item = random.sample(game_logic.items, 1)

    if rand == 1:
        console.print(f"""
        You walk into the mysterious room, not sure what to expect.
        The room is nicely decorated with many different cave paintings,
        perhaps describing the culture of the people who live in the
        jungle? In the center of the room stands an offering bowl.
        You peer inside to find a [i #9D00FF]{random_granted_item}[/i #9D00FF] inside! Just your luck. 
    
    """, style=reward_style)
        if random_granted_item in ["survival knife", "grappling hook", "rope"] and random_granted_item in inventory and len(inventory) < 3:
            console.print(f"You already have a {random_granted_item} in your inventory, cannot be obtained!", style=reward_style)
        elif len(inventory) < 3:
            inventory.append(random_granted_item)
        else:
            console.print("Insufficient inventory space!", style=reward_style)

        return inventory, health, stamina

    elif rand == 2:
        console.print("""
        You walk into the mysterious room, not sure what to expect.
        Upon entering, you see a gorgeous fountain, with a shimmering
        pool of water clear as crystal. As you take a sip from the
        fountain, you feel your injuries heal and your pain fades
        
        [i #FF3131]Health[/i #FF3131] restored!
    """, style=reward_style)
        health = 10
        return inventory, health, stamina

    elif rand == 3:
        console.print("""
        You walk into the mysterious room, not sure what to expect.
        Upon entering, you see an old tree that stretches its branches
        all across the room. The tree almost seems to be glowing with
        light. Large golden fruit hang from the branches, giving off
        a sweet aroma. As you take a bite, you feel your strength
        rushing back into your body and your fatigue fades.
        
        [i #FFFF33]Stamina[/i #FFFF33] replenished!
    """, style=reward_style)
        stamina = 10
        return inventory, health, stamina


if __name__ == "__main__":
    reward_room(["med spray", "ration"], 5, 5)
