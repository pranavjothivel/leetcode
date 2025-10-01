class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 != 0:
            result.append(0)
        
        counter = 1
        while len(result) != n:
            positive_val = counter
            negative_val = (-1) * counter

            result.extend([positive_val, negative_val])

            counter += 1
        
        return result