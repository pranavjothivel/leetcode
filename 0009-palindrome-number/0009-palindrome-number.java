class Solution {
    public boolean isPalindrome(int x) {
        String orig = Integer.toString(x);
        String rev = "";
        for (int i = Integer.toString(x).length() - 1; i >= 0; i--) {
            rev = rev + Integer.toString(x).substring(i, i+1);
        }
        return orig.equals(rev);
    }
}