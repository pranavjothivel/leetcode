class Solution {
    // public int hammingWeight(int n) {
    //     return Integer.bitCount(n);
    // }
    public int hammingWeight(int n) {
        int bits = 0;
        // n is unsigned
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                bits++;
            }
        }
        return bits;
    }
}