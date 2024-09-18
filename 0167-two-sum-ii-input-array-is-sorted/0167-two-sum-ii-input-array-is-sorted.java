class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] indices = new int[2];
        for (int i = 0; i < numbers.length; i++) {
            for (int k = i + 1; k < numbers.length; k++) {
                int i1 = numbers[i];
                int i2 = numbers[k];
                
                if ((i1 + i2) == target) {
                    indices[0] = i + 1;
                    indices[1] = k + 1;

                    return indices;
                }
            }
        }
        return indices;
    }
}