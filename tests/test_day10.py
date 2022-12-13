# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# System imports
from pathlib import Path

from advent import day10

DATA_PATH = Path(__file__).parent.joinpath("data")


def test_frequency() -> None:
    """Test Day 10 - Cathode-Ray Tube"""
    file = DATA_PATH.joinpath("day10_data.txt")
    with open(file) as f:
        data = f.readlines()
    day = day10.Day()

    assert 13140 == day.program(data)
