class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # words = s.strip().split(' ')
        # newS = ''
        # for i in range(0, k):
        #     newS += words[i]
        #     if i != k - 1:
        #         newS += ' '
        # return newS

        return " ".join(s.split(' ')[:k])