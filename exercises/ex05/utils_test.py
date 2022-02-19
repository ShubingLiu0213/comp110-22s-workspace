"""A test of utils."""

__author__ = "730508266"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """A test of empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_all_evens() -> None:
    """A test of many numbers."""
    numbers: list[int] = [6, 8, 2, 4]
    assert only_evens(numbers) == [6, 8, 2, 4]


def test_only_evens_many_numbers() -> None:
    """A test of many numbers again."""
    numbers: list[int] = [3, 4, 5, 6]
    assert only_evens(numbers) == [4, 6]


def test_sub_empty() -> None:
    """A test of an empty a_list."""
    a_list: list[int] = []
    assert sub(a_list, 0, 0) == []


def test_sub_start_negative_numbers() -> None:
    """A test of sub function with negative start."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -1, 3) == [10, 20, 30]


def test_sub_many_numbers_again() -> None:
    """A test of sub function with many nimbers."""
    a_list: list[int] = [45, 34, 4, 67, 9, 50, 30]
    assert sub(a_list, 2, 6) == [4, 67, 9, 50]


def test_concat_empty() -> None:
    """A test of empty lists."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_many_numbers() -> None:
    """A test of many numbers."""
    first: list[int] = [3, 45, 6, 78]
    second: list[int] = [4, 67, 8, 59, 6]
    assert concat(first, second) == [3, 45, 6, 78, 4, 67, 8, 59, 6]


def test_concat_many_numbers_with_a_number() -> None:
    """A test of different size lists."""
    first: list[int] = [4, 56, 7]
    second: list[int] = [899]
    assert concat(first, second) == [4, 56, 7, 899]