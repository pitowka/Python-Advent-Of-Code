from re import Pattern
from collections.abc import Callable

from commons.inputs import Input
from abc import ABC, abstractmethod
import re


class Command(ABC):
    @abstractmethod
    def process(self, command: str, grid: list[list[int]]) -> None:
        pass


class BaseCommand(Command):
    def __init__(self,
                 regex: str,
                 action: Callable) -> None:  # Callable[[list[list[bool]], tuple[int, int, int, int]], None]
        self.pattern: Pattern[str] = re.compile(regex)
        self.action = action

    def process(self, command: str, grid: list[list[int]]) -> None:
        match = self.pattern.match(command)
        if match:
            self.action(grid, tuple(map(int, list(match.groups()))))


class TurnOn1(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'turn on (\d+),(\d+) through (\d+),(\d+)', TurnOn1.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] = 1


class TurnOff1(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'turn off (\d+),(\d+) through (\d+),(\d+)', TurnOff1.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] = 0


class Toggle1(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'toggle (\d+),(\d+) through (\d+),(\d+)', Toggle1.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] = 1 if grid[x][y] == 0 else 0


class GroupedCommand1(Command):
    def __init__(self) -> None:
        super().__init__()
        self.commands: list[Command] = [TurnOn1(), TurnOff1(), Toggle1()]

    def process(self, command: str, grid: list[list[int]]) -> None:
        for c in self.commands:
            c.process(command, grid)


class TurnOn2(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'turn on (\d+),(\d+) through (\d+),(\d+)', TurnOn2.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] += 1


class TurnOff2(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'turn off (\d+),(\d+) through (\d+),(\d+)', TurnOff2.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] = max(0, grid[x][y] - 1)


class Toggle2(BaseCommand):
    def __init__(self) -> None:
        super().__init__(r'toggle (\d+),(\d+) through (\d+),(\d+)', Toggle2.action)

    @staticmethod
    def action(grid: list[list[int]], coordinates: tuple[int, int, int, int]) -> None:
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                grid[x][y] += 2


class GroupedCommand2(Command):
    def __init__(self) -> None:
        super().__init__()
        self.commands: list[Command] = [TurnOn2(), TurnOff2(), Toggle2()]

    def process(self, command: str, grid: list[list[int]]) -> None:
        for c in self.commands:
            c.process(command, grid)


def part1() -> None:
    grid: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    gc: Command = GroupedCommand1()
    list(map(lambda x: gc.process(x, grid), Input('inputs/day6').as_list()))

    print(sum(list(map(sum, grid))))


def part2() -> None:
    grid: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    gc: Command = GroupedCommand2()
    list(map(lambda x: gc.process(x, grid), Input('inputs/day6').as_list()))

    print(sum(list(map(sum, grid))))


part1()
part2()
