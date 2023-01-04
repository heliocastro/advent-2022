# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 8: Treetop Tree House --- The expedition comes across a peculiar patch of tall trees all
planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a
reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this,
you need to count the number of trees that are visible from outside the grid when looking directly
along a row or column.
"""

# System imports
from typing import Dict, List, Tuple

# Application imports
from advent.base import Base


class Day(Base):
    """
    Day 8 Class: Treetop House
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
        if self.data:
            trees, score = self.treetop(self.data)
            print(f"Number of visible trees are {trees}")
            print(f"Visibility score: {score}")

    def treetop(self, data: List[str]) -> Tuple[int, int]:
        """Get the number of visible trees and the score of visibility

        Args:
            data (List[str]): The tree dataset

        Returns:
            Tuple[int, int]: Trees visible and visibility score
        """
        # Size of "tree matrix"
        size: Dict[str, int] = dict(x=len(data[0]), y=len(data))

        score: int = 0

        # Start pushing the number of left/right edges
        visible: int = size["x"] * 2 + (size["y"] - 2) * 2

        # Assembly as a linear
        trees: str = "".join(data)

        for pos_y in range(1, size["y"] - 1):
            for pos_x in range(1, size["x"] - 1):
                is_visible: bool = False
                # Add all neighbours in columns and row
                neighbours: List[int] = []

                for x in range(0, size["x"]):
                    neighbours.append(int(trees[(pos_y * size["x"]) + x]))
                if self.is_visible(pos_x, neighbours):
                    is_visible = True
                h_score: int = self.scenic_score(pos_x, neighbours)

                neighbours.clear()
                for y in range(0, size["y"]):
                    neighbours.append(int(trees[(y * size["x"] + pos_x)]))
                if self.is_visible(pos_y, neighbours):
                    is_visible = True
                v_score: int = self.scenic_score(pos_y, neighbours)

                if is_visible:
                    visible += 1

                if (h_score * v_score) > score:
                    score = h_score * v_score
        return visible, score

    def is_visible(self, tree_pos: int, data: List[int]) -> bool:
        """Verify if Tree is visible in the tree row

        Args:
            tree_pos (int): The tree position to analyze
            data (List[int]): The tree line ( vertical or horizontal )

        Returns:
            bool: _description_
        """
        left: bool = True
        right: bool = True

        for tree in range(0, tree_pos):
            if data[tree] >= data[tree_pos]:
                left = False
        for tree in range(tree_pos + 1, len(data)):
            if data[tree] >= data[tree_pos]:
                right = False

        if left or right:
            return True

        return False

    def scenic_score(self, tree_pos: int, data: List[int]) -> int:
        """Calculate the score of visibility

        Args:
            tree_pos (int): _description_
            data (List[int]): _description_

        Returns:
            int: Socire of visibility
        """

        left: int = 0
        right: int = 0

        for tree in range(tree_pos, 0, -1):
            left += 1
            if data[tree - 1] >= data[tree_pos]:
                break
        for tree in range(tree_pos + 1, len(data)):
            right += 1
            if data[tree] >= data[tree_pos]:
                break

        return right * left
