class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_str = "".join(c.lower() for c in s if c.isalnum())
        return sanitized_str == sanitized_str[::-1]