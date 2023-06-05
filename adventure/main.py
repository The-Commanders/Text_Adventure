from game import *
from intro import introduction
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
## class imports
from environments.jungle import Jungle
from environments.river import River
from environments.desert import Desert
from environments.ruins_entrance import RuinsEntrance
from environments.ruins_halls import Ruins_Halls
from environments.ruins_final_room import RuinsFinalRoom
from intro import introduction
from ending import final



def main():

    # Anthony's testing code' start
    game = introduction()
    # game = GameLogic('survival knife')
    jungle = Jungle("jungle", console.print, Prompt.ask)
    desert = Desert("desert", console.print, Prompt.ask)
    river = River("river")
    ruins_ent = RuinsEntrance("ruins_entrance", console.print, Prompt.ask)
    ruins_hall = Ruins_Halls("ruins_halls")
    ruins_fr = RuinsFinalRoom("final_room")
    envs = [jungle, river, desert, ruins_ent, ruins_hall, ruins_fr]
    # game.add_environment(jungle)
    # game.add_environment(river)
    # game.add_environment(desert)
    # game.add_environment(ruins_ent)
    # game.add_environment(ruins_hall)
    # game.add_environment(ruins_fr)

    for env in envs:
        game.add_environment(env)

    game.traverse_environments()
    final(game.health, game.stamina)
    # game.game_over()
    # game.trigger_random_event(jungle)
    # game.trigger_random_event(river)
    # game.trigger_random_event(desert)
    # game.trigger_random_event(ruins_ent)
    # game.trigger_random_event(ruins_hall)
    # game.trigger_random_event(ruins_fr)
    # print(f"this is an instance of Jungle: {jungle}")
    # print(game)
    # str(game)
    # game.traverse_environments()
    # Anthony's testing code end

    ## Deiosha's testing code
    # game = GameLogic()
    # river = River("river")
    # game.add_environment(river)
    # game.traverse_environments()


    ## Brenden's testing code
    # game = GameLogic("rope")
    # desert = Desert("desert", console.print, Prompt.ask)
    #
    # game.add_environment(desert)
    # game.traverse_environments()


if __name__ == "__main__":
    main()
