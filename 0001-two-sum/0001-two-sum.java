class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] sols = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    sols[0] = i;
                    sols[1] = j;
                }
            }
        }
        return sols;
    }
}