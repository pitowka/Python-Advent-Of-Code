import hashlib

puzzle_input: str = 'ckczppom'


def part1() -> None:
    idx: int = 0
    while not (hashlib.md5(f'{puzzle_input}{idx}'.encode()).hexdigest().startswith('00000')):
        idx += 1
    print(idx)


def part2() -> None:
    idx: int = 0
    while not (hashlib.md5(f'{puzzle_input}{idx}'.encode()).hexdigest().startswith('000000')):
        idx += 1
    print(idx)


part1()
part2()
