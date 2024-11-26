class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums_count = 0
        for i in range(1, arr[-1] + k + 1):
            if i not in arr:
                missing_nums_count += 1
            if missing_nums_count == k:
                return i
        return -1