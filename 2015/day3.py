from commons.inputs import Input


def part1() -> None:
    print(
        len(
            buildings(Input('inputs/day3').as_string())))


def part2() -> None:
    print(
        len(
            buildings(Input('inputs/day3').as_string()[::2])
            .union(buildings(Input('inputs/day3').as_string()[1::2]))))


def buildings(directions: str) -> set[tuple[int, int]]:
    homes: list[tuple[int, int]] = [(0, 0)]
    for c in directions:
        last_building: tuple[int, int] = homes[-1]

        (x, y) = last_building
        new_building: tuple[int, int] = (
            x + (1 if c == '>' else (-1 if c == '<' else 0))
            , y + (1 if c == '^' else (-1 if c == 'v' else 0)))
        homes.append(new_building)

    return set(homes)


part1()
part2()
