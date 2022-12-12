# SPDX-FileCopyrightText: Copyright (C) <2022> Helio Chissini de Castro
# SPDX-License-Identifier: BSD Clause-3

import importlib

import click


@click.group()
def messages() -> None:
    """Help messages stub"""


@click.command()
@click.argument("day_of_month", type=click.INT)
@click.option("-f", "--filename", "filename")
def day(day_of_month: int, filename: str = "") -> None:
    """Do Day Work"""
    module = f"advent.day{day_of_month}"
    day_module = importlib.import_module(module)
    if not filename:
        filename = f"resources/day{day_of_month}.txt"
    day_chore = day_module.Day(filename)
    day_chore.process()


messages.add_command(day)


if __name__ == "__main__":
    messages()
