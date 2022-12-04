# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey.
Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to
be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one
of the two compartments. The Elf that did the packing failed to follow this rule for exactly one
item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but
they need your help finding the errors. Every item type is identified by a single lowercase or
uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack
always has the same number of items in each of its two compartments, so the first half of the
characters represent items in the first compartment, while the second half of the characters
represent items in the second compartment.
"""

# System Imports
from typing import List

# Application impoerts
from advent.base import Base


class Day(Base):
    """
    Day 3 Class: Rucksack Reorganization
    """

    def process(self) -> None:
        """Process the game

        Args:
            data (str): List of calories per Elf

        Returns:
            int: The amount of calories spent by the Elfs
        """

        priorities = self.priorities(self.data)
        print(f"The number of screwed Elf priorities is {priorities}")
        priorities = self.badges(self.data)
        print(f"Number of group badges priorities is {priorities}")

    def prio_value(self, letter: int) -> int:
        """Calculate correct value based on ASCII table
        - Lowercase item types a through z have priorities 1 through 26.
        - Uppercase item types A through Z have priorities 27 through 52.

        Args:
            letter (int): Then netry letter

        Returns:
            int: Resulting value
        """
        # Play easy with ascci lowercase first
        if letter >= 97:
            return letter - 96  # 97 is 'a', so we reduce 97 to match prio 1

        return letter - 38  # Now uppercase which 'A' is 65

    def priorities(self, data: List[str]) -> int:
        """Rucksack duplicate iten priority finder

        Args:
            data (str): List of rucksacks

        Returns:
            int: Sum of the priorities
        """
        priorities: int = 0

        for rucksack in data:
            split = len(rucksack) // 2
            left, right = rucksack[:split], rucksack[split:]
            # Get straight the ascii number
            item = ord((set(left) & set(right)).pop())
            priorities += self.prio_value(item)

        return priorities

    def badges(self, data: List[str]) -> int:
        """Badges need to be recover

        Args:
            data (List[str]): List of rucksacks

        Returns:
            int: Sum of badges
        """
        badges_priorities: int = 0

        size = len(data)
        for i in range(0, size, 3):
            if (size - i) < 3:
                break
            group: List[str] = [data[i], data[i + 1], data[i + 2]]
            item = ord((set(group[0]) & set(group[1]) & set(group[2])).pop())
            badges_priorities += self.prio_value(item)

        return badges_priorities
