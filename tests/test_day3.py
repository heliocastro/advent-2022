# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day3


@pytest.fixture
def rucksack_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_priorities(rucksack_data):
    """Test Day 3 - Rucksack priorities"""
    day = day3.Day()
    assert 157 == day.priorities(rucksack_data)


def test_badges(rucksack_data):
    """Test Day 3 - Rucksack badges"""
    day = day3.Day()
    assert 70 == day.badges(rucksack_data)
