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
from environments.ruins_final_room import Ruins_Final_Room



def main():

    # Anthony's testing code' start
#     game = GameLogic("survival knife")
#     jungle = Jungle("jungle")
#     desert = Desert("desert")
#     river = River("river")
#     ruins_ent = RuinsEntrance("ruins_entrance")
#     ruins_hall = Ruins_Halls("ruins_halls")
#     ruins_fr = Ruins_Final_Room()
#     envs = [jungle, desert, river, ruins_ent, ruins_hall, ruins_fr]
    # game.add_environment(jungle)
    # game.add_environment(desert)
#     game.add_environment(ruins_ent)
    # for env in envs:
    #     game.add_environment(env)
    # game.traverse_environments()
    # game.trigger_random_event(jungle)
    # game.trigger_random_event(desert)
#     game.trigger_random_event(ruins_ent)
    # print(f"this is an instance of Jungle: {jungle}")
#     print(game)
#     str(game)
    # game.traverse_environments()
    # Anthony's testing code end

    ## Deiosha's testing code
    # game = GameLogic()
    # river = River("river")
    # game.add_environment(river)
    # game.traverse_environments()


    ## Brenden's testing code
#     game = GameLogic()
#     desert = Desert("desert")
#     game.add_environment(desert)
#     game.traverse_environments()



if __name__ == "__main__":
    main()
