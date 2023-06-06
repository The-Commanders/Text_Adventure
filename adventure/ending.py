from rich.console import Console
from rich.prompt import Prompt
import random
from intro import random_color


def final(health, stamina):
    console = Console()
    console.print(f"""
[b white]
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                                                                    |
    | Your journey is nearing its end. You have overcome countless obstacles and pushed  |
    | through challenging scenarios. Your body aches, but you are so close to your goal, |
    |    the idol is in the next room over. Obtain it, and your mission is complete!     |
    |                                                                                    |
    | You enter the room containing the idol. Elegant paintings cover the walls, with a  |
    | bright yellow light shinning onto a particular pedestal at the edge of the room.   |
    |        As you walk over you see 3 identical idols, all in different colors.        |
    |                                                                                    |
     \                                                                                  /
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

    colors_2 = ["red", "blue", "green", "yellow", "purple", "black", "white"]
    random_colors = random.sample(colors_2, 2)

    if random_color in random_colors:
        random_colors.remove(random_color)
        random_colors.append(random.choice([color for color in colors_2 if color != random_color]))
    if random_colors[0] == random_colors[1]:
        random_colors = random.sample(colors_2, 2)

    # print(random_color, random_colors)

    final_decision = Prompt.ask(f"""[b white]
    Your final decision has come, before you are 3 idols all in different colors.
    You cant fail now after you've come so far, but how can you choose?
    There must be a way. Please type the color idol you will take.
    
    [{random_colors[0]}]{random_colors[0]}[/{random_colors[0]}], [{random_color}]{random_color}[/{random_color}], [{random_colors[1]}]{random_colors[1]}[/{random_colors[1]}]
""")

    while True:
        if final_decision == f"{random_color}":
            console.print(f"""[b yellow]
    [green]You chose correctly[/green]
    As you pick up the idol, you can feel its power flow through you,
    unbelievable strength, endless knowledge, and a sense of accomplishment.
    The journey is over, time to call [#FF5F1F]Ishmael[/#FF5F1F] to get you out of here!
    
    You survived with: 
    [i #FF3131]{health}[/i #FF3131] health
    [i #FFFF33]{stamina}[/i #FFFF33] stamina""")
            break

        elif final_decision == f"{random_colors[0]}" or final_decision == f"{random_colors[1]}":
            console.print("""[b white]
    [red]You chose incorrectly[/red]
    You pick up the false idol and it crumbles in your hands. The ruins around you
    start to crumble, and the room caves in on you. How can you possibly escape now?
    You were so close, but unfortunately, its
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼                                    
""")
            break
        else:
            final_decision = Prompt.ask(f"""[b white]
    Please write the color you want to pick.
    [{random_colors[0]}]{random_colors[0]}[/{random_colors[0]}], [{random_color}]{random_color}[/{random_color}], [{random_colors[1]}]{random_colors[1]}[/{random_colors[1]}]
""")
    play_again = Prompt.ask("""[b yellow]
    Play again?
    Type yes or quit.
    """, default="yes")
    while play_again:
        if play_again == "yes":
            pass
        elif play_again == "quit":
            console.print("""[bold yellow]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |                                                                                    |
     |                                                                                    |
     |                               Thank you for playing!                               |
     |                                                                                    |
     |                           Check out this project github                            |
     |                                                                                    |
     |                  https://github.com/The-Commanders/Text_Avdeventure                |
     |                                                                                    |
      \                                                                                  /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
            return
        else:
                play_again = Prompt.ask("""[b yellow]
    Please type "yes" or "quit"
    """)


if __name__ == "__main__":
    final()
