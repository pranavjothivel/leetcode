class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 4 in base-2
        # 10 -> one bit
        # 16 in base-2
        # 10000 -> one bits
        return n >= 0 and n.bit_count() == 1