# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several
Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID
number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other,
they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce
duplicated effort, the Elves pair up and make a big list of the section assignments for each pair.
"""

# System Imports
from typing import List, Tuple

# Application impoerts
from advent.base import Base


class Day(Base):
    """
    Day 4 Class: Camp Cleanup
    """

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): List of calories per Elf

        Returns:
            int: Number of overlaps on the cleanup system
        """
        overlap, overlap_all = self.overlaps(self.data)
        print(f"Number of overlaps in assignments: {overlap}")
        print(f"Number of overlaps at all in assignments: {overlap_all}")

    def overlaps(self, data: List[str]) -> Tuple[int, int]:
        """Calculate the overlaps of the "well defined" Elf assignemnt work

        Args:
            data (List[str]): List of assignments

        Returns:
            int: NUmber of overlapped assignments
        """
        overlap: int = 0
        overlap_all: int = 0

        for assignment in data:
            elf_1: List[int] = list(map(int, assignment.split(",")[0].split("-")))
            elf_2: List[int] = list(map(int, assignment.split(",")[1].split("-")))

            # Test left and right elfs major x minor twice, reversing
            # It can have a better implementation, but his do the job
            if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or (
                elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]
            ):
                overlap += 1
            if elf_1[0] >= elf_2[0] and elf_1[0] <= elf_2[1]:
                overlap_all += 1
            elif elf_2[0] >= elf_1[0] and elf_2[0] <= elf_1[1]:
                overlap_all += 1

        return overlap, overlap_all
