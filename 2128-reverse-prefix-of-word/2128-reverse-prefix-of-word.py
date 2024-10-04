class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if (word.find(ch) == -1 or word == ''):
            return word

        idx = word.find(ch) + 1
        return word[:idx][::-1] + word[idx:]
