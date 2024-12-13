class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minStartValue = 1 
        currentSum = 0
        minPrefixSum = 0

        for num in nums:
            currentSum += num
            minPrefixSum = min(minPrefixSum, currentSum)

        if minPrefixSum < 0:
            minStartValue = 1 - minPrefixSum

        return minStartValue