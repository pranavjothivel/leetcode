class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution = 0
        for num in nums:
            solution = num ^ solution
        return solution