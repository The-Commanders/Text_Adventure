from adventure.environments.jungle import Jungle

def test_jungle_name():

    jungle = Jungle("jungle")
    actual = jungle.name
    expected = "jungle"

    assert actual == expected

def test_jungle_name_int():
    pass


