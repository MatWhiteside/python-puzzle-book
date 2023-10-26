from __future__ import annotations


class RussianDoll:
    def __init__(
            self,
            size: int,
            colour: str,
            child_doll: RussianDoll | None = None
    ) -> None:

        self.size = size
        self.colour = colour
        self.child_doll = child_doll

    def get_number_of_children(self) -> int:
        if self.child_doll is None:
            return 0
        return 1 + self.child_doll.get_number_of_children()

    def print_unpack(self) -> None:
        print(
            f"Unpacking a {self.colour} doll of size: {self.size} with {self.get_number_of_children()} nested dolls inside."
        )


def unpack_dolls(doll: RussianDoll) -> int:
    print(f"Total number of dolls unpacked: {inner_unpack_dolls(doll)}")


def inner_unpack_dolls(doll: RussianDoll) -> int:

    doll.print_unpack()

    if doll.child_doll is None:
        return 1

    return 1 + inner_unpack_dolls(doll.child_doll)


doll_size_one = RussianDoll(1, "red", None)
doll_size_two = RussianDoll(2, "blue", doll_size_one)
doll_size_three = RussianDoll(3, "green", doll_size_two)
doll_size_four = RussianDoll(4, "purple", doll_size_three)
doll_size_five = RussianDoll(5, "grey", doll_size_four)
unpack_dolls(doll_size_five)
