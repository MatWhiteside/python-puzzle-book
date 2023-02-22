def tap_code(input_code: str) -> str:
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
    tap_code_map = {v: k for k, v in tap_code_map.items()}

    # Break up the tap code into separate words, convert each word and then
    # concatenate the result together
    result = ""
    words = input_code.split("   ")

    for word in words:
        result += "".join(tap_code_map[c] for c in word.split("  "))
        result += " "

    # Strip off the trailing space
    return result.strip()


print(tap_code(".. ..  .. ....  ..... .  . .....   .... .....  .... ...   ... ..  ... ....  .... ..  . .....   ... .....  .... .....  ..... .....  ..... .....  ... .  . .....  .... ..."))
print(tap_code(". .  . ..  . ...  . ....  . .....  .. .  .. ..  .. ...  .. ....  .. .....  ... .  ... ..  ... ...  ... ....  ... .....  .... .  .... ..  .... ...  .... ....  .... .....  ..... .  ..... ..  ..... ...  ..... ....  ..... ....."))
print(tap_code(".. ...  .. ....   .. ...  .. ...."))
