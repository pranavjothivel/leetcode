class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_chars = []
        for c in s:
            if c.isalnum():
                s_chars.append(c.lower())
        
        sanitized_str = "".join(s_chars)
        
        l, r = 0, len(sanitized_str) - 1

        while l < r:
            if sanitized_str[l] != sanitized_str[r]:
                return False
            l += 1
            r -= 1
        return True