class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # numsLength = len(nums)
        # return nums[numsLength // 2]
        return nums[len(nums) // 2]
        