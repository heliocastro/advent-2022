# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 12: Hill Climbing Algorithm --- 
You try contacting the Elves using your handheld device, but
the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows
the local area from above broken into a grid; the elevation of each square of the grid is given by a
single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the
highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should
get the best signal (E). Your current position (S) has elevation a, and the location that should get
the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each
step, you can move exactly one square up, down, left, or right. To avoid needing to get out your
climbing gear, the elevation of the destination square can be at most one higher than the elevation
of your current square; that is, if your current elevation is m, you could step to elevation n, but
not to elevation o. (This also means that the elevation of the destination square can be much lower
than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is
near the middle. You could start by moving down or right, but eventually you'll need to head toward
the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the
path exits each square moving up (^), down (v), left (<), or right (>). The location that should get
the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get
the best signal?
"""

# System imports
import logging
from typing import List

# from threading import Thread

# Libraries
# pylint: disable=redefined-builtin
from rich import print

# Application imports
from advent.base import Base
from advent.utils.point import Point


class Day(Base):
    """
    Day 12: Hill Climbing Algorithm
    """

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): Input data

        Returns:
            int: Output value
        """

        data = self.hill(self.data)
        logging.info(data)

    def hill(self, data: List[str]) -> int:
        if self.data is None:
            self.data = data.copy()

        for line_number, line in enumerate(data):
            origin: Point | None = None
            if "S" in line:
                pos = line.index("S")
                origin = Point(pos, line_number)
                break

        if not origin:
            return -1

        visited: List[Point] = [origin]
        self.thread_walking(visited)
        print(visited)
        return 0

    def thread_walking(self, visited: List[Point] | None = None) -> None:
        # path_thread: List[Thread] = []self.data[dest.y][dest.x]

        point: Point = visited[len(visited) - 1]
        dest: Point | None = None

        while True:
            logging.info(f"{visited}")
            if point.y - 1 >= 0:
                dest = Point(point.x, point.y - 1)
                if 'E' == self.data[dest.y][dest.x]:
                    break
                if self.compare_next(point, dest) and dest not in visited:
                    visited.append(dest)
                    self.thread_walking(visited)
                else:
                    break
            if point.y + 1 <= len(self.data):
                dest = Point(point.x, point.y + 1)
                if 'E' == self.data[dest.y][dest.x]:
                    break
                if self.compare_next(point, dest) and dest not in visited:
                    visited.append(dest)
                    self.thread_walking(visited)
                else:
                    break
            if point.x - 1 >= 0:
                dest = Point(point.x - 1, point.y)
                if 'E' == self.data[dest.y][dest.x]:
                    break
                if self.compare_next(point, dest) and dest not in visited:
                    visited.append(dest)
                    self.thread_walking(visited)
                else:
                    break
            if point.x + 1 <= len(self.data[0]):
                dest = Point(point.x + 1, point.y)
                if 'E' == self.data[dest.y][dest.x]:
                    break
                if self.compare_next(point, dest) and dest not in visited:
                    visited.append(dest)
                    self.thread_walking(visited)
                else:
                    break

    def compare_next(self, origin: Point, dest: Point) -> bool:
        origin_ascii = ord(self.data[origin.y][origin.x])
        if origin_ascii == ord("S"):
            origin_ascii = ord("a")
        dest_ascii = ord(self.data[dest.y][dest.x])
        print(
            f"origin: {self.data[origin.y][origin.x]} - {origin_ascii},dest: {self.data[dest.y][dest.x]} - {dest_ascii}"
        )
        return dest_ascii in (origin_ascii, origin_ascii + 1)
