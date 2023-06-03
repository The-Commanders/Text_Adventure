import pytest
import random
from adventure.environments.ruins_entrance import RuinsEntrance


def test_ruins_entrance_name():

    ruins_entrance = RuinsEntrance("ruins_entrance")
    actual = ruins_entrance.name
    expected = "ruins_entrance"

    assert actual == expected

