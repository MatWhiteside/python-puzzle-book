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


def unpack_dolls(doll: RussianDoll) -> int:
    # Your implementation here



doll_size_one = RussianDoll(1, "red", None)
doll_size_two = RussianDoll(2, "blue", doll_size_one)
doll_size_three = RussianDoll(3, "green", doll_size_two)
doll_size_four = RussianDoll(4, "purple", doll_size_three)
doll_size_five = RussianDoll(5, "grey", doll_size_four)
unpack_dolls(doll_size_five)