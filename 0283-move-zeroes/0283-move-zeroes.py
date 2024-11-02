class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers approach
        # have a starting index for non-zero numbers
        # fill with zeroes from this pointer to the end

        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        
        for j in range(i, len(nums)):
            nums[j] = 0