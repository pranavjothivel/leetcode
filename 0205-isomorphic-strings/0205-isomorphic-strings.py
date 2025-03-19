from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for c_s, c_t in zip(s, t):
            if c_s in mapping_s_to_t and mapping_s_to_t[c_s] != c_t:
                return False
            if c_t in mapping_t_to_s and mapping_t_to_s[c_t] != c_s:
                return False
            
            mapping_s_to_t[c_s] = c_t
            mapping_t_to_s[c_t] = c_s
        return True