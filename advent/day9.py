# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 9: Rope Bridge --- This rope bridge creaks as you walk along it. You aren't sure how old it
is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by
the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by
modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the
head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the
knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle
input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and
tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching)
"""

# System imports
from copy import copy
from typing import List, Tuple

# Application imports
from advent.base import Base
from advent.utils.point import Point


class Day(Base):
    """
    Day 9 Class: Rope Bridge
    """

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): List of calories per Elf

        Returns:
            int: Number of overlaps on the cleanup system
        """

        rope_lenght, snake = self.rope_lenght(self.data)
        print(f"Visited on Part1: {rope_lenght}")
        print(f"Visited with snake Part2: {snake}")

    def rope_lenght(self, data: List[str]) -> Tuple[int, int]:
        head: Point = Point(0, 0)
        tail: Point = Point(0, 0)
        single_knot: int = 0
        multiple_knots: int = 0
        visited: List[Point] = [Point(0, 0)]

        max_x, max_y = 0, 0

        for move in data:
            direction: str = move.split()[0]
            moves: int = int(move.split()[1])

            for _ in range(0, moves):
                if direction == "R":
                    head.x += 1
                    if not self.adjacent(head, tail):
                        tail.x += 1
                        tail.y = head.y
                        if tail not in visited:
                            visited.append(copy(tail))
                elif direction == "L":
                    head.x -= 1
                    if not self.adjacent(head, tail):
                        tail.x -= 1
                        tail.y = head.y
                        if tail not in visited:
                            visited.append(copy(tail))
                            single_knot += 1
                elif direction == "U":
                    head.y += 1
                    if not self.adjacent(head, tail):
                        tail.x = head.x
                        tail.y += 1
                        if tail not in visited:
                            visited.append(copy(tail))
                            single_knot += 1
                elif direction == "D":
                    head.y -= 1
                    if not self.adjacent(head, tail):
                        tail.x = head.x
                        tail.y -= 1
                        if tail not in visited:
                            visited.append(copy(tail))
                            single_knot += 1
                if head.x > max_x:
                    max_x = head.x
                if head.y > max_y:
                    max_y = head.y

        for y in range(max_y, -1, -1):
            line: str = ""
            for x in range(0, max_x + 1):
                if y == 0 and x == 0:
                    line += "s"
                elif Point(x, y) in visited:
                    line += "#"
                else:
                    line += "."

        return single_knot, multiple_knots

    def adjacent(self, head: Point, tail: Point) -> bool:
        for x in range(-1, 2):
            for y in range(-1, 2):
                adj: Point = Point(tail.x + x, tail.y + y)
                if adj == head:
                    return True
        return False
