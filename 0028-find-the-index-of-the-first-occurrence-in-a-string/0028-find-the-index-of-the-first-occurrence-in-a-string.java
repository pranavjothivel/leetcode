class Solution {
    public int strStr(String haystack, String needle) {
        // Handle the edge case where needle is an empty string
        if (needle.isEmpty()) {
            return 0;
        }

        int haystackLength = haystack.length();
        int needleLength = needle.length();

        // Iterate through the haystack, ensuring we do not exceed the bounds
        for (int i = 0; i <= haystackLength - needleLength; i++) {
            // Check if the substring matches the needle
            if (haystack.substring(i, i + needleLength).equals(needle)) {
                return i;
            }
        }

        // Return -1 if the needle is not found
        return -1;
    }
}