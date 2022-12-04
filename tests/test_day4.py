# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day4


@pytest.fixture
def assignment_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]


def test_assignments(assignment_data):
    """Test Day 4 - Camp Cleanup"""
    day = day4.Day()
    assert 2, 4 == day.overlaps(assignment_data)
