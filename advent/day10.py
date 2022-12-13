# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 10: Cathode-Ray Tube --- You avoid the ropes, plunge into the river, and swim to shore.

The Elves yell something about meeting back up with them upriver, but the river is too loud to tell
exactly what they're saying. They finish crossing the bridge and disappear from view.

Situations like this must be why the Elves prioritized getting the communication system on your
handheld device working. You pull it out of your pack, but the amount of water slowly draining from
a big crack in its screen tells you it probably won't be of much immediate use.

Unless, that is, you can design a replacement for the device's video system! It seems to be some
kind of cathode-ray tube screen and simple CPU that are both driven by a precise clock circuit. The
clock circuit ticks at a constant rate; each tick is called a cycle.

Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which
starts with the value 1. It supports only two instructions:

addx V takes two cycles to complete. After two cycles, the X register is increased by the value V.
(V can be negative.) noop takes one cycle to complete. It has no other effect.
"""

# System imports
import logging
from typing import List

# Libraries
# pylint: disable=redefined-builtin
from rich import print

# Application imports
from advent.base import Base


class Day(Base):
    """
    Day 10: Cathode-Ray Tube
    """

    cycles: int = 0
    register_x: int = 1
    # Cycle step starts on 20, then jump to each 40
    step: int = 20
    strenght: int = 0
    crt: str = ""

    def process(self) -> None:
        """Process the assignments

        Args:
            data (str): Input data

        Returns:
            int: Output value
        """

        strenght = self.program(self.data)

        print(f"Your current Cathode Strenght is {strenght}.\n")

        for i in range(0, 6):
            line = (
                (self.crt[i * 40 : (i + 1) * 40])
                .replace("#", "[bold yellow2]#[/bold yellow2]")
                .replace(".", " ")
            )
            print(line)

    def program(self, data: List[str]) -> int:
        """Process ops and calculate the cycle freq

        Args:
            data (List[str]): Input data

        Returns:
            int: Result freq
        """

        for entry in data:
            op: List[str] = entry.split()
            if op[0].startswith("noop"):
                logging.debug(f"Start cycle {self.cycles}: begin executing noop")
                self.inc_cycle()
                logging.debug(f"End of cycle {self.cycles}: finish executing noop")
            elif op[0].startswith("addx"):
                logging.debug(f"Start cycle {self.cycles}: begin executing addx {int(op[1])}")
                self.inc_cycle()
                self.inc_cycle()
                self.register_x += int(op[1])
                logging.debug(
                    f"End of cycle {self.cycles}: finish executing addx"
                    f"{int(op[1])} (Register X is now {self.register_x}"
                )

        return self.strenght

    def inc_cycle(self) -> None:
        self.cycles += 1
        # print(f"Cycle: {self.cycles}, register_x: {self.register_x}")
        if self.cycles % self.step == 0:
            self.strenght += self.cycles * self.register_x
            self.step += 40

        logging.debug(f"During cycle {self.cycles}: CRT draws pixel in position {self.cycles - 1}")

        pos: int = (self.cycles - 1) % 40
        if pos >= self.register_x - 1 and pos <= self.register_x + 1:
            self.crt += "#"
        else:
            self.crt += "."

        scanline: int = 0
        if self.cycles > 40:
            scanline = 40 * int(self.cycles / 40)
        logging.debug(f"Current CRT row: {self.crt[scanline:]}\n")
