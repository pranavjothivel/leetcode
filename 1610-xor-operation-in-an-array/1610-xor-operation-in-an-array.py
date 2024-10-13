class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            num = start + 2 * i
            xor ^= num
        return xor