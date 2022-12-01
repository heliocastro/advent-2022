# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day1


@pytest.fixture
def calorie_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]


def test_calorie_counting(calorie_data):
    """Test Day 1 - Calorie Counting"""
    day = day1.Day()
    day.strong_elfs(calorie_data)

    elf1 = day.elfs[0][0]
    elf2 = day.elfs[1][0]
    elf3 = day.elfs[2][0]
    three_elfs = elf1 + elf2 + elf3

    assert elf1 == 24000
    assert three_elfs == 45000
