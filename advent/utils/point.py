# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

from dataclasses import dataclass


@dataclass
class Point:
    """
    Create a simple base representation of geometic coordinates using dataclass
    """

    x: int = 0
    y: int = 0
