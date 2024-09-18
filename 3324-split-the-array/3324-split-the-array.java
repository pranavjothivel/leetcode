import java.util.Map;
import java.util.HashMap;

class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        Map<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int n : nums) {
            hashMap.put(n, hashMap.getOrDefault(n, 0) + 1);
        }
        for (Map.Entry e : hashMap.entrySet()) {
            if ((int) e.getValue() > 2) {
                return false;
            }
        }
        return true;
    }
}