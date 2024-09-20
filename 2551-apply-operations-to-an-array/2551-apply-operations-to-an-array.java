class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        
        // Step 1: Apply the operation
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] = nums[i] * 2;
                nums[i + 1] = 0;
            }
        }
        
        // Step 2: Shift non-zero elements to the front
        int[] result = new int[n];
        int index = 0;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                result[index++] = nums[i];
            }
        }
        
        // Return the array with zeros moved to the end
        return result;
    }
}