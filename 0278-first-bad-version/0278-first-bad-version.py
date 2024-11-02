# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        left, right = 1, n

        while left < right:
            mid = (left + right) >> 1 # midpt calc using bit shifting
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
