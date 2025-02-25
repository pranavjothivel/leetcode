class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        while (i < len(word1) and i < len(word2)):
            res += word1[i]
            res += word2[i]
            i += 1
        res += word1[i:len(word1)] if i < len(word1) else word2[i:len(word2)]
        return res