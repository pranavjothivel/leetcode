class Solution {
    public int[] applyOperations(int[] nums) {
        int size = nums.length;
        
        for (int i = 0; i < size - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] = nums[i] * 2;
                nums[i + 1] = 0;
            }
        }
        
        int[] array = new int[size];
        int index = 0;
        
        for (int i = 0; i < size; i++) {
            if (nums[i] != 0) {
                array[index] = nums[i];
                index++;
            }
        }
        
        return array;
    }
}