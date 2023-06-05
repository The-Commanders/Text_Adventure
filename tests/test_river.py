import random
from colorama import Fore, Style
import pytest
from adventure.environments.river import River

@pytest.fixture
def river():
    return River("Test River")

def test_display_text(capsys, river):
    river.display_text("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test message"

# def test_item_collection(capsys, river):
#     river.item_collection()
#     captured = capsys.readouterr()
#     expected_output = """Items in the game:
# - First aid spray
# - Ration"""
#     assert captured.out.strip() == expected_output

def test_situation_event_one(monkeypatch, capsys, river):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    river.situation_event_one()
    captured = capsys.readouterr()
    assert "You swim across the river." in captured.out

def test_danger_event_one(monkeypatch, capsys, river):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    river.danger_event_one()
    captured = capsys.readouterr()
    assert "You engage in a fierce battle." in captured.out

def test_puzzle_event_one(monkeypatch, capsys, river):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    river.puzzle_event_one()
    captured = capsys.readouterr()
    assert "Riddle:" in captured.out

# def test_play_game(monkeypatch, capsys, river):
#     monkeypatch.setattr('builtins.input', lambda _: 'next')
#     river.play_game()
#     captured = capsys.readouterr()
#     assert "You have embarked on the River Challenge!" in captured.out