# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to
deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that
only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove
where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by
December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab
any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star.
Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air;
the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin
taking inventory of their supplies.
One important consideration is food - in particular, the number of Calories each Elf is
carrying (your puzzle input).
"""

# System imports
from typing import List, Tuple

# Application impoerts
from advent.base import Base


class Day(Base):
    """
    Day 1 Class: Calorie Counting
    """

    elfs: List[Tuple[int, int]] = []

    def process(self) -> None:
        """Process the calories list

        Args:
            data (str): List of calories per Elf

        Returns:
            int: The amount of calories spent by the Elfs
        """
        self.strong_elfs(self.data)

        total = 0
        for i in range(0, 3):
            total = total + self.elfs[i][0]

        elf = self.elfs[0]
        print(f"The stronger Elf is {elf[1]} carrying {elf[0]}")
        elf = self.elfs[1]
        print(f"The second stronger Elf is {elf[1]} carrying {elf[0]}")
        elf = self.elfs[2]
        print(f"The Third stronger Elf is {elf[1]} carrying {elf[0]}")
        print(f"They are carrying {total} calories")

    def strong_elfs(self, data: List[str]) -> None:
        """Load the elf calories list
        The Elves take turns writing down the number of Calories contained by the various meals,
        snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates
        their own inventory from the previous Elf's inventory (if any) by a blank line.

        By the time you calculate the answer to the Elves' question, they've already realized that
        the Elf carrying the most Calories of food might eventually run out of snacks.

        To avoid this unacceptable situation, the Elves would instead like to know the total
        Calories carried by the top three Elves carrying the most Calories. That way, even if one of
        those Elves runs out of snacks, they still have two backups.

        Args:
            data (str): List of calories per Elf
        """

        total = 0
        elf = 1
        for calories in data:
            if calories.strip():
                total = total + int(calories.strip())
            else:
                self.elfs.append((total, elf))
                elf = elf + 1
                total = 0
        self.elfs.append((total, elf))
        self.elfs.sort(reverse=True)
