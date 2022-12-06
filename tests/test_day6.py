# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day6


@pytest.fixture
def base_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        [7, 19, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"],
        [5, 23, "bvwbjplbgvbhsrlpgdmjqwftvncz"],
        [6, 23, "nppdvjthqldpwncqszvftbrmjlhg"],
        [10, 29, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"],
        [11, 26, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"],
    ]


def test_signal_marker(base_data):
    """Test Day 5 - Tunning Trouble"""
    day = day6.Day()
    for signal in base_data:
        assert signal[0] == day.datastream_marker(signal[2])


def test_message_marker(base_data):
    """Test Day 5 - Tunning Trouble"""
    day = day6.Day()
    for signal in base_data:
        assert signal[1] == day.datastream_marker(signal[2], 14)
