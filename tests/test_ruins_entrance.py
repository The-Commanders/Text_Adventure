import pytest
import random
from adventure.environments.ruins_entrance import RuinsEntrance


class RuinsEntrance:
    def __init__(self, name):
        self.name = name


@pytest.mark.parametrize("input_values", [
    ['meow'],  # Correct association for 'cat'
    ['tail'],  # Correct association for 'dog'
    ['tribe'],  # Correct association for 'jungle'
    ['banana']  # Correct association for 'monkey'
])
def test_word_association_correct(input_values, monkeypatch, capsys):
    random.seed(42)  # Set a fixed seed for predictable results
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    obj = RuinsEntrance(RuinsEntrance("Ruins"))  # Provide the required 'name' argument
    obj.word_association()
    captured = capsys.readouterr()

    expected_output = "Correct association!"
    assert captured.out.strip().endswith(expected_output)


@pytest.mark.parametrize("input_values", [
    ['bark'],  # Incorrect association for 'cat'
    ['play'],  # Incorrect association for 'dog'
    ['rain'],  # Incorrect association for 'jungle'
    ['whiskers']  # Incorrect association for 'monkey'
])
def test_word_association_incorrect(input_values, monkeypatch, capsys):
    random.seed(42)  # Set a fixed seed for predictable results
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    obj = RuinsEntrance(RuinsEntrance("Ruins"))  # Provide the required 'name' argument
    obj.word_association()
    captured = capsys.readouterr()

    expected_output = "Incorrect association."
    assert captured.out.strip().endswith(expected_output)
