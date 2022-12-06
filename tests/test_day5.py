# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day5


@pytest.fixture
def stack_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "    [D]",
        "[N] [C]",
        "[Z] [M] [P]",
        " 1   2   3",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


def test_stacks(stack_data):
    """Test Day 5 - Supply Stacks"""
    day = day5.Day()
    crane9000, crane9001 = day.crane_suffer(stack_data)
    assert "CMZ" == crane9000
    assert "MCD" == crane9001
