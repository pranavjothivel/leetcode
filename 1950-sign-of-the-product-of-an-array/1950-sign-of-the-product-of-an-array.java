class Solution {
    public int arraySign(int[] nums) {
        int productSign = 1;
        for (int num : nums) {
            if (num < 0) {
                // ovverwrites productSign only if num is < 0
                // and productSign becomes '1' when two negatives
                // multiply and cancel signs
                productSign *= -1;
            }
            else if (num == 0) {
                return 0;
            }
        }
        return productSign;
    }
}