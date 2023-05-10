def to_roman(number: int) -> str:
    mumber = int(number)

    if number < 1:
        return None

    else:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
            "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
            "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
            "VI", "VII", "VIII", "IX"]

        thousands = m[number // 1000]
        hundreds = c[(number % 1000) // 100]
        tens = x[(number % 100) // 10]
        ones = i[number % 10]

        roman = thousands + hundreds + tens + ones

        return roman.replace(' ', '')


def from_roman(string: str) -> int:
    pass
