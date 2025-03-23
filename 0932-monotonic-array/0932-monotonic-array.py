class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for j in range(1, len(nums)):
            i = j - 1
            if nums[i] > nums[i+1]:
                increasing = False
            elif nums[i] < nums[i+1]:
                decreasing = False
        return increasing or decreasing