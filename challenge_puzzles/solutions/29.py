tap_code_map = {
    "a": ". .",
    "b": ". ..",
    "c": ". ...",
    "d": ". ....",
    "e": ". .....",
    "f": ".. .",
    "g": ".. ..",
    "h": ".. ...",
    "i": ".. ....",
    "j": ".. .....",
    "l": "... .",
    "m": "... ..",
    "n": "... ...",
    "o": "... ....",
    "p": "... .....",
    "q": ".... .",
    "r": ".... ..",
    "s": ".... ...",
    "t": ".... ....",
    "u": ".... .....",
    "v": "..... .",
    "w": "..... ..",
    "x": "..... ...",
    "y": "..... ....",
    "z": "..... .....",
}


def tap_code_to_english(input_code: str) -> str:
    tap_code_map_inv = {v: k for k, v in tap_code_map.items()}

    if len(input_code) == 0:
        return ""

    # Break up the tap code into separate words, convert each word and then
    # concatenate the result together
    words_as_tap_code = input_code.split("   ")
    return " ".join(
        [
            "".join(
                tap_code_map_inv[letter_as_tap_code]
                for letter_as_tap_code in word_as_tap_code.split("  ")
            )
            for word_as_tap_code in words_as_tap_code
        ]
    )


print(
    tap_code_to_english(
        ".. ..  .. ....  ..... .  . .....   .... .....  .... ...   ... ..  ... ....  .... ..  . .....   ... .....  .... .....  ..... .....  ..... .....  ... .  . .....  .... ..."
    )
)
print(
    tap_code_to_english(
        ". .  . ..  . ...  . ....  . .....  .. .  .. ..  .. ...  .. ....  .. .....  ... .  ... ..  ... ...  ... ....  ... .....  .... .  .... ..  .... ...  .... ....  .... .....  ..... .  ..... ..  ..... ...  ..... ....  ..... ....."
    )
)
print(tap_code_to_english(".. ...  .. ....   .. ...  .. ...."))
print(tap_code_to_english(". ...  ... ....  ... ....  ... ."))
print(tap_code_to_english(""))
