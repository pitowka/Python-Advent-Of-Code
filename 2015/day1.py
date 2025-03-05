from commons.inputs import Input
from collections import Counter


def part1() -> None:
    cnt: Counter = Counter(Input('inputs/day1')
                           .first_line()
                           .rstrip()
                           )
    print(cnt['('] - cnt[')'])


def part2() -> None:
    idx: int = 0
    floor: int = 0
    instr: str = Input('inputs/day1').first_line().rstrip()

    while floor >= 0:
        floor += 1 if instr[idx] == '(' else -1
        idx += 1

    print(idx)


part1()
part2()
