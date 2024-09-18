import java.util.Map;
import java.util.HashMap;

class Solution {
    public int singleNumber(int[] nums) {
        int solution = -1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry numEntry : map.entrySet()) {
            if ((int) numEntry.getValue() < 2) {
                solution = (int) numEntry.getKey();
                return solution;
            }
        }
        return solution;
    }
}