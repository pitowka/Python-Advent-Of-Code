from commons.inputs import Input
from abc import ABC, abstractmethod
import re


class Check(ABC):
    @abstractmethod
    def test(self, to_test: str) -> bool:
        return False


class HasEnoughVowels(Check):
    def test(self, to_test: str) -> bool:
        return len([item for item in list(to_test) if item in ['a', 'e', 'i', 'o', 'u']]) >= 3


class HasDoubledLetter(Check):
    def test(self, to_test: str) -> bool:
        return re.search(r'(.)\1', to_test) is not None


class NotContains(Check):
    def test(self, to_test: str) -> bool:
        return (re.search(r'ab', to_test) is None
                and re.search(r'cd', to_test) is None
                and re.search(r'pq', to_test) is None
                and re.search(r'xy', to_test) is None)


class HasPairOfDouble(Check):
    def test(self, to_test: str) -> bool:
        return re.search(r'(..).*\1', to_test) is not None


class HasRepeatedLetter(Check):
    def test(self, to_test: str) -> bool:
        return re.search(r'(.).\1', to_test) is not None


class CompositeCheck(Check):
    def __init__(self, checks: list[Check]) -> None:
        super().__init__()
        self.checks: list[Check] = checks

    def test(self, to_test: str) -> bool:
        return all(map(lambda c: c.test(to_test), self.checks))


class IsPrettyPart1(CompositeCheck):
    def __init__(self) -> None:
        super().__init__([HasEnoughVowels(), HasDoubledLetter(), NotContains()])


class IsPrettyPart2(CompositeCheck):
    def __init__(self) -> None:
        super().__init__([HasPairOfDouble(), HasRepeatedLetter()])


def part1() -> None:
    print(
        len(
            list(
                filter(lambda s: IsPrettyPart1().test(s), Input('inputs/day5').as_list()))))


def part2() -> None:
    print(
        len(
            list(
                filter(lambda s: IsPrettyPart2().test(s), Input('inputs/day5').as_list()))))


part1()
part2()
