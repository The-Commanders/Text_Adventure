# rich
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
# environments
from adventure.intro import introduction
from adventure.environments.jungle import Jungle
from adventure.environments.river import River
from adventure.environments.desert import Desert
from adventure.environments.ruins_entrance import RuinsEntrance
from adventure.environments.ruins_halls import Ruins_Halls
from adventure.environments.ruins_final_room import RuinsFinalRoom
from adventure.ending import final
# game logicpyte

console = Console()


def main():

    game = introduction()

    jungle = Jungle(console.print, Prompt.ask)
    desert = Desert(console.print, Prompt.ask)
    river = River(console.print, Prompt.ask)
    ruins_ent = RuinsEntrance(console.print, Prompt.ask)
    ruins_hall = Ruins_Halls(console.print, Prompt.ask)
    ruins_fr = RuinsFinalRoom(console.print, Prompt.ask)

    envs = [jungle, river, desert, ruins_ent, ruins_hall, ruins_fr]

    for env in envs:
        game.add_environment(env)

    game.traverse_environments()

    final(game.health, game.stamina)


if __name__ == "__main__":
    main()
