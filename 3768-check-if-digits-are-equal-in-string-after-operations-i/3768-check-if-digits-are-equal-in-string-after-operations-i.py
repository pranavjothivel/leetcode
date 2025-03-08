class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while (len(s) != 2):
            res = ""
            for i in range(len(s) - 1):
                first = int(s[i])
                second = int(s[i + 1])
                num = (first + second) % 10
                res += str(num)
            s = res
        return s[0] == s[1]
            