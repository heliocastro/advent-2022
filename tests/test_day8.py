# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

# pylint: disable=missing-module-docstring
import pytest

from advent import day8


@pytest.fixture
def base_data():
    """Fixture of test data

    Returns:
        _type_: List of data
    """
    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]


def test_treeview(base_data):
    """Test Day 8 - Treetop House"""
    day = day8.Day()
    visibility, _ = day.treetop(base_data)
    assert 21 == visibility


def test_scenic_score(base_data):
    """Test Day 8 - Treetop House"""
    day = day8.Day()
    _, score = day.treetop(base_data)
    assert 8 == score
