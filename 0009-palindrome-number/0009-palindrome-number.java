class Solution {
    public boolean isPalindrome(int x) {
        String intX = Integer.toString(x);
        for (int i = 0; i < intX.length(); i++) {
            if (intX.charAt(i) != intX.charAt(intX.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}