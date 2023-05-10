import re


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
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for i in range(len(string)):
        if i > 0 and roman_dict[string[i]] > roman_dict[string[i-1]]:
            result += roman_dict[string[i]] - 2 * roman_dict[string[i-1]]
        else:
            result += roman_dict[string[i]]

    return result
