# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack
storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round,
the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a
winner for that round is selected:
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the
same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle
input) that they say will be sure to help you win. "The first column is what your opponent is going
to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is
called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper,
and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum
 of your scores for each round. The score for a single round is the score for the shape you
 selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
 round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the
score you would get if you were to follow the strategy guide.
"""

# System imports
from typing import List

# Application impoerts
from advent.base import Base


class Day(Base):
    """
    Day 2 Class: Rock Paper Scissors
    """

    # Simple two letter to state winner situations
    winner: List[str] = ["A Y", "B Z", "C X"]
    loser: List[str] = ["A Z", "B X", "C Y"]
    draws: List[str] = ["A X", "B Y", "C Z"]

    def process(self) -> None:
        """Process the game

        Args:
            data (str): List of calories per Elf

        Returns:
            int: The amount of calories spent by the Elfs
        """

        print(f"Your regular score is {self.game(self.data)}")
        print(f"Your doctored score is {self.game(self.data, True)}")

    def game(self, data: List[str], fixed: bool = False) -> int:
        """Calculate the strategy guide

        Args:
            data (str): List of calories per Elf
        """
        points: int = 0

        for game_move in data:
            if len(game_move) < 3:
                continue

            if fixed:
                game_move = self.fixed_game(game_move)

            # Calculate points per piece
            if game_move[2] == "X":
                points = points + 1
            elif game_move[2] == "Y":
                points = points + 2
            elif game_move[2] == "Z":
                points = points + 3

            # Verify draw
            if game_move in self.draws:
                points = points + 3
                continue

            if game_move in self.winner:
                points = points + 6

        return points

    def fixed_game(self, data: str) -> str:
        """The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the
        second column says how the round needs to end: X means you need to lose, Y means you need
        to end the round in a draw, and Z means you need to win. Good luck!"

        Args:
            data (str): _description_

        Returns:
            str: Doctored data
        """

        # Dictionaire to substitution
        subst = {"A": "X", "B": "Y", "C": "Z"}

        # Draw
        if data[2] == "Y":
            data = data.replace("Y", subst[data[0]])
            return data
        if data[2] == "X":
            for move in self.loser:
                if move[0] == data[0]:
                    return move
        elif data[2] == "Z":
            for move in self.winner:
                if move[0] == data[0]:
                    return move

        return data
