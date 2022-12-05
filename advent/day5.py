# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies
are stored in stacks of marked crates, but because the needed supplies are buried under many other
crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the
crates get crushed or fall over, the crane operator will rearrange them in a series of
carefully-planned steps. After the crates are rearranged, the desired crates will be at the top
of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot
to ask her which crate will end up where, and they want to be ready to unload them as soon as
possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement
procedure (your puzzle input).
"""

# System Imports
import copy
from typing import List, Tuple

# Application imports
from advent.base import Base


class Day(Base):
    """
    Day 5 Class: Supply Stacks
    """

    stacks: List[List[str]] = []

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): List of calories per Elf

        Returns:
            int: Number of overlaps on the cleanup system
        """

        cratemover_9000, cratemover_9001 = self.crane_suffer(self.data)

        print(f"Your crane stacks container data is {cratemover_9000}.")
        print(f"Your crane stacks container data is {cratemover_9001}.")

    def crane_suffer(self, data: List[str]) -> Tuple[str, str]:
        """Return the crane letter list

        Args:
            data (List[str]): _description_

        Returns:
            str: _description_
        """

        matrix_size: int = 0
        for numbers in data:
            if "1" not in numbers:
                continue
            matrix_size = int(numbers[len(numbers) - 3 :].strip())
            for _ in range(0, matrix_size):
                self.stacks.append([])
            break

        # Add the vector list of containers
        pos: int = 0

        for pos, entry in enumerate(data):
            if "1" in entry:
                break

            for listpos in range(0, matrix_size):
                if len(entry) < 3:
                    break
                container = entry[:3].strip()
                if container == "":
                    entry = entry[4:]
                    continue
                self.stacks[listpos].append(entry[:3].strip().strip("[").strip("]"))
                entry = entry[4:]

        # Pass along only the moves (ignore last empty line adding 2)
        cratemover_9000 = self.cratemover_9000(data[pos:])
        cratemover_9001 = self.cratemover_9001(data[pos:])

        return cratemover_9000, cratemover_9001

    def cratemover_9000(self, data: List[str]) -> str:
        """Play along with the container moves.
        For the sake of simple exercise, we are not validating
        the data entry, but for didatic purpose, we always need
        to remember to validate the file

        Args:
            data (List[str]): Move data

        Returns:
            str: Resulting stack
        """
        stacks = copy.deepcopy(self.stacks)
        for entry in data:
            if not entry.startswith("move"):
                continue
            oper = entry.split()
            # Remember dear elves, lists always starts on 0
            _move, _from, _to = int(oper[1]), int(oper[3]) - 1, int(oper[5]) - 1
            for _ in range(0, _move):
                item = stacks[_from].pop(0)
                stacks[_to].insert(0, item)

        results = ""
        for reslist in stacks:
            results += reslist[0]

        return results

    def cratemover_9001(self, data: List[str]) -> str:
        """As you watch the crane operator expertly rearrange the crates, you notice the process
        isn't following your prediction. Some mud was covering the writing on the side of the crane,
        and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

        The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather
        seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

        Args:
            data (List[str]): Move data

        Returns:
            str: Resulting stack
        """
        stacks = copy.deepcopy(self.stacks)
        for entry in data:
            if not entry.startswith("move"):
                continue
            oper = entry.split()
            # Remember dear elves, lists always starts on 0
            _move, _from, _to = int(oper[1]), int(oper[3]) - 1, int(oper[5]) - 1
            item = stacks[_from][:_move]
            stacks[_from] = stacks[_from][_move:]
            item.extend(stacks[_to])
            stacks[_to] = item

        results = ""
        for reslist in stacks:
            results += reslist[0]

        return results
