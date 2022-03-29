"""A test of dictionary."""

__author__ = "730508266"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_chars() -> None:
    """A test of invert function with characters."""
    old_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(old_dict) == {'z': 'a', 'y': 'b', 'x': 'c'} 


def test_invert_empty() -> None:
    """A test of empty invert function."""
    old_dict: dict[str, str] = {}
    assert invert(old_dict) == {}


def test_invert_KeyError() -> None:
    """A test of KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_one() -> None:
    """A Test of one color."""
    color: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(color) == "yellow"


def test_favorite_color_two() -> None:
    """A Test of 2 colors."""
    color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(color) == "blue"


def test_favorite_color_three() -> None:
    """A Test of 3 colors."""
    color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Uffe": "pink"}
    assert favorite_color(color) == "blue"


def test_count_empty() -> None:
    """A test of empty count."""
    counter: list[str] = []
    assert count(counter) == {}


def test_count_onekey() -> None:
    """A test of one key."""
    counter: list[str] = ["orange", "orange", "orange", "orange"]
    assert count(counter) == {"orange": 4}


def test_count_threekeys() -> None:
    """A test of three keys."""
    counter: list[str] = ["pink", "blue", "blue", "yellow"]
    assert count(counter) == {"pink": 1, "blue": 2, "yellow": 1}