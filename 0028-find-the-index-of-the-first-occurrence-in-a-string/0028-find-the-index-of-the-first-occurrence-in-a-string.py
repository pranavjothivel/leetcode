class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0

        while l <= len(haystack) - len(needle):
            if haystack[l:].startswith(needle):
                return l
            else:
                l += 1
        
        return -1