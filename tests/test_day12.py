# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day12


@pytest.fixture
def base_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]


def test_hill(base_data):
    """Test Day 12 - Hill Climbing Algorithm"""
    day = day12.Day()
    visited = day.hill(base_data)
    assert 31 == visited
