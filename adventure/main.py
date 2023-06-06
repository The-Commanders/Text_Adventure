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
# game logic
from adventure.game import GameLogic

console = Console()


def main():
    # Anthony's testing code' start
    game = introduction()
    # game = GameLogic('survival knife')
    jungle = Jungle(console.print, Prompt.ask)
    # desert = Desert(console.print, Prompt.ask)
    # river = River()
    # ruins_ent = RuinsEntrance(console.print, Prompt.ask)
    # ruins_hall = Ruins_Halls()
    # ruins_fr = RuinsFinalRoom()
    # envs = [jungle, river, desert, ruins_ent, ruins_hall, ruins_fr]

    # jungle = Jungle()
    jungle.event_one()
    # jungle.event_two()
    # jungle.event_three()
    # jungle.event_four()
    # river = River()
    # river.event_one()
    # river.event_two()
    # river.event_three()
    # desert = Desert()
    # desert.event_one()
    # desert.event_two()
    # desert. event_three()
    # ruins_ent = RuinsEntrance()
    # ruins_ent.event_one()
    # ruins_ent.event_two()
    # ruins_ent.event_three()
#     ruins_hall = Ruins_Halls()
#     ruins_hall.event_one()
#     ruins_hall.event_two()
#     ruins_hall.event_three()


    # ruins_fr = RuinsFinalRoom()
    # ruins_fr.event_one()
    # ruins_fr.event_two()
    # ruins_fr.event_three()
    # envs = [jungle, river, desert, ruins_ent, ruins_hall, ruins_fr]

    # Anthony's testing code start
    # game = GameLogic('survival knife')

    # game.add_environment(jungle)
    # game.add_environment(river)
    # game.add_environment(desert)
    # game.add_environment(ruins_ent)
    # game.add_environment(ruins_hall)
    # game.add_environment(ruins_fr)
    #
    # for env in envs:
    #     game.add_environment(env)
    #
    # game.traverse_environments()
    # final(game.health, game.stamina)
    
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
