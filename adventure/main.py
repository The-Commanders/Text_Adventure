from game import *
from intro import introduction
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
## class imports
from environments.jungle import Jungle
from environments.river import River


def main():

    ## Anthony's testing code' start
    # game = GameLogic()
    # jungle = Jungle("jungle")
    # game.add_environment(jungle)
    # print(f"this is an instance of Jungle: {jungle}")
    # print(game)
    # str(game)
    # game.traverse_environments()
    ## Anthony's testing code end

    ## Deiosha's testing code
    game = GameLogic()
    river = River("river")
    game.add_environment(river)
    game.traverse_environments()


if __name__ == "__main__":
    main()
