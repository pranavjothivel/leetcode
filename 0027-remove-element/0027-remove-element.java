class Solution {
    public int removeElement(int[] nums, int val) {
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                // this line modifies the array in-place
                // by replacing the index (starting at 0)
                // with each value not equivalent to 'val'
                nums[counter] = nums[i];
                counter++;
            }
        }

        return counter;
    }
}