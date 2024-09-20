class Solution {
    public int removeDuplicates(int[] nums) {
        // left is also the counter for duplicates
        int left = 1;

        for (int right = 1; right < nums.length; right++) {
            // compare right number with number behind it
            // comparing left to right has the edge case of going out of bounds
            // on last index comparison
            if (nums[right] != nums[right - 1]) {
                nums[left] = nums[right];
                left++;
            }
        }
        
        return left;
    }
}