from commons.inputs import Input


class Present:
    def __init__(self, dimensions: str):
        (self.a, self.b, self.c) = list(map(int, dimensions.split('x')))

    def surface(self) -> int:
        return (2 * (self.a * self.b
                     + self.a * self.c
                     + self.b * self.c)
                + min(self.a * self.b
                      , self.a * self.c
                      , self.b * self.c))

    def ribbon(self) -> int:
        return (sum(sorted([self.a, self.b, self.c])[:2]) * 2 +
                self.a * self.b * self.c)

    def __str__(self) -> str:
        return f'a = {self.a}, b = {self.b}, c = {self.c}'


def part1() -> None:
    print(
        sum(
            list(
                map(
                    lambda s: Present(s).surface(),
                    Input('inputs/day2').as_list()
                )
            )
        )
    )


def part2() -> None:
    print(
        sum(
            list(
                map(
                    lambda s: Present(s).ribbon(),
                    Input('inputs/day2').as_list()
                )
            )
        )
    )


part1()
part2()
