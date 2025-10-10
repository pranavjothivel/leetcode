class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            if row[l] <= target <= row[r]:
                while l <= r:
                    midpoint = (l + r) // 2
                    if row[midpoint] == target:
                        return True
                    elif row[midpoint] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                continue
        return False