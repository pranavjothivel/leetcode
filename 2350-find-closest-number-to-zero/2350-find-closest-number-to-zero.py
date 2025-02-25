class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = inf

        for n in nums:
            # handles case if both have same absolute value
            if abs(n) < abs(ans) or (abs(n) == abs(ans) and n > ans):
                ans = n
                # print(ans)
        return ans
    # O(1) space
    # O(n) time