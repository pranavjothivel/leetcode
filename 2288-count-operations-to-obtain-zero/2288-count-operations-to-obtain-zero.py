class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0

        while (num1 != 0 and num2 != 0):
            if num1 >= num2:
                num1 -= num2
                ops +=1
            else:
                num2 -= num1
                ops += 1
        return ops