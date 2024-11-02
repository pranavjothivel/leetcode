class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat = []
        for i in range(2 * n):
            concat.append(nums[i % n])
        return concat