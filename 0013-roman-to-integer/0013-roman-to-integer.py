class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = 0
        symbols = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
            }
        # for first_char, next_char in zip(s, s[1:]):
        #     if (symbols[first_char] < symbols[next_char]):
        #         roman_integer -= symbols[first_char]
        #     else:
        #         roman_integer += symbols[first_char]
        for i in range(len(s) - 1):
            if symbols[s[i]] < symbols[s[i + 1]]:
                roman_integer -= symbols[s[i]]
            else:
                roman_integer += symbols[s[i]]

        # Add the value of the last character since loop iterates up to len(s) - 1
        roman_integer += symbols[s[-1]]
        return roman_integer