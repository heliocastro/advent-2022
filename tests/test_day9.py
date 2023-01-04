# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day9


@pytest.fixture
def single_knot_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]


@pytest.fixture
def multiple_knots_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]


def test_single_knot(single_knot_data):
    """Test Day 9 - Rope Lenght"""
    day = day9.Day()
    visited, _ = day.rope_lenght(single_knot_data)
    assert 13 == visited


def test_mulyiple_knots(multiple_knots_data):
    """Test Day 9 - Rope Lenght - Part2"""
    day = day9.Day()
    _, visited = day.rope_lenght(multiple_knots_data)
    assert 36 == visited
