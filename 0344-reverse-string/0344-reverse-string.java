class Solution {
    public void reverseString(char[] s) {
        for (int i = 0; i < s.length / 2; i++) {
            char swapChar = s[s.length - 1 - i];
            s[s.length - 1 - i] = s[i];
            s[i] = swapChar;
        }
    }
}