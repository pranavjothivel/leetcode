class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i <= k:
                k += 1
            elif i > k:
                break
        
        return k