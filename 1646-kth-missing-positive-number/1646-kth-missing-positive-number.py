class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current = 1
        hashset = set(arr)

        while True:
            if current not in hashset:
                missing_count += 1
                if missing_count == k:
                    return current
            current += 1