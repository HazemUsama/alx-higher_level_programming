#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0
    for idx, char in enumerate(roman_string):
        try:
            if roman[roman_string[idx]] < roman[roman_string[idx + 1]]:
                ans -= roman[char]
                continue
        except IndexError:
            pass
        ans += roman[char]
    return ans
