# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day9


@pytest.fixture
def base_data():
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


def test_ropes(base_data):
    """Test Day 9 - Rope Lenght"""
    day = day9.Day()
    visited, _ = day.rope_lenght(base_data)
    assert 13 == visited
