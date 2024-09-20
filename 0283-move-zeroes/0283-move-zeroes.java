class Solution {
    public void moveZeroes(int[] nums) {
        int counter = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[counter] = nums[i];
                counter++;
            }
        }

        for (int i = counter; i < nums.length; i++) {
            // counter is the number of non-zeroes in the array
            // and the starting position from which to fill zeroes
            nums[i] = 0;
        }
    }
}