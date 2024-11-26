class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums = []
        counter = 1
        while (len(missing_nums) <= k):
            if counter not in arr:
                missing_nums.append(counter)
            counter += 1
        return missing_nums[k-1]