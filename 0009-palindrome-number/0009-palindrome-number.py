# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if (x < 0):
#             return False
#         reversed = 0
#         x_original = x
#         while(x > 0):
#             reversed = (reversed * 10) + (x % 10)
#             x = x // 10
#         return reversed == x_original

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)