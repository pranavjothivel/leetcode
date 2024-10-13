class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for num in range(n):
            xor ^= start + 2 * num
        return xor