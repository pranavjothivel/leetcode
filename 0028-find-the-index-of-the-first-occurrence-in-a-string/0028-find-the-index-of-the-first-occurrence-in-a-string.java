class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;

        int haystackLength = haystack.length();
        int needleLength = needle.length();

        // helps to prevent loop for going out of bounds
        int lengthDifferential = haystackLength - needleLength;

        for (int i = 0; i <= lengthDifferential; i++) {
            if (haystack.substring(i, i + needle.length()).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}