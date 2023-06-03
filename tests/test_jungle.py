import pytest
from adventure.game import InvalidDataTypeError
from adventure.environments.jungle import Jungle


def test_jungle_name():

    jungle = Jungle("jungle")
    actual = jungle.name
    expected = "jungle"

    assert actual == expected


def test_jungle_name_int():
    with pytest.raises(InvalidDataTypeError) as e:
        jungle = Jungle(1)
    assert str(e.value) == "Data type must be a string!"



