import java.util.Arrays;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);  // Sort the array in-place
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;  // Found a duplicate
            }
        }
        return false;  // No duplicates found
    }
}