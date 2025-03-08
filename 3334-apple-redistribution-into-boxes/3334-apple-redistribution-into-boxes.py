class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(key = lambda a: -a)
        apple_sum = sum(apple)

        num = 0

        for box in capacity:
            if apple_sum > 0:
                apple_sum -= box
                num +=1
        
        return num