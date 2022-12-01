# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
Advennt of Code Base utility functions

As per default regular input on all Advent of Code commits comes in txt format,
make standard base class always ready the related input in txt format
"""

import sys
from typing import List


class Base:
    """
    Base Class - Utility Functions
    """

    def __init__(self, filename: str = ""):
        self.data: List[str] = []
        if filename:
            self.readdata(filename)

    def readdata(self, filename: str) -> None:
        """
        Read a text input data file

        Args:
            filename (str): the filename path
        """
        try:
            # pylint: disable=unspecified-encoding
            with open(filename, "r") as inputfile:
                self.data = inputfile.readlines()
        except IOError:
            print("Input file could not be found.")
            sys.exit(1)
