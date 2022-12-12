# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as
the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big
do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to
run a system update:

$ system-update --please --pretty-please-with-sugar-on-top Error: No space left on device Perhaps
you can delete some files to make space for the update?
"""

# System imports
from typing import List

# Application imports
from advent.base import Base


class Day(Base):
    """
    Day 7 Class: No space Left
    """

    total: int = 0
    freed: int = 0
    disksize: int = 70000000

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): List of calories per Elf

        Returns:
            int: Number of overlaps on the cleanup system
        """

        self.dir(self.data)
        print(f"Your directory size are {self.total}")
        print(f"Your minimal delete dir is {self.freed}")

    def dir(self, data: List[str], dirsize: List[int] = []) -> int:
        """Find file total in directories

        Args:
            data (List[str]): The data input
            dirsize (List[int]): List of directory sizes

        Returns:
            int: Total of files
        """
        total: int = 0
        while len(data) > 0:
            entry: str = data.pop(0)
            if entry.startswith("$ cd"):
                if "/" in entry:
                    continue
                if ".." in entry:
                    break
                total += self.dir(data, dirsize)
                continue
            if entry.startswith("$ ls") or entry.startswith("dir"):
                continue
            size, _ = entry.split()
            total += int(size)

        if total < 100000:
            self.total += total
        dirsize.append(total)
        dirsize.sort(reverse=True)
        for ds in dirsize:
            freed = self.disksize - total + ds
            if freed <= 30000000:
                break
            self.freed = ds

        return total
