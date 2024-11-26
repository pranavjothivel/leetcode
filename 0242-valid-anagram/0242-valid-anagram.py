class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq_s = {}
        for l in s:
            freq_s[l] = freq_s.get(l, 0) + 1
        freq_t = {}
        for l in t:
            freq_t[l] = freq_t.get(l, 0) + 1
        return freq_s == freq_t
        # time: O(m + n)
        # space: O(1)