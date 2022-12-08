# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day7


@pytest.fixture
def base_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..    ",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def test_dir_size(base_data):
    """Test Day 7 - No Space Left"""
    day = day7.Day()
    day.dir(base_data)
    assert 95437 == day.total
    assert 24933642 == day.freed
