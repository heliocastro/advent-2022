# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day2


@pytest.fixture
def game_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "A Y",
        "B X",
        "C Z",
    ]


def test_rock_paper_scissor(game_data):
    """Test Day 2 - Rock, Paper Scissors"""
    day = day2.Day()
    assert 15 == day.game(game_data)
    assert 12 == day.game(game_data, True)
