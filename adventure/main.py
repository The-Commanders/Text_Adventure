from game import *
from environments.jungle import Jungle


def main():
    # Anthony's testing code' start
    game = GameLogic()
    jungle = Jungle("jungle")
    game.add_environment(jungle)
    print(f"this is an instance of Jungle: {jungle}")
    print(game)
    str(game)
    game.traverse_environments()
    # Anthony's testing code end


if __name__ == "__main__":
    main()
    # pass