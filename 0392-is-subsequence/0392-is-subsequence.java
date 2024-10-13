class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.isEmpty()) {
            return true;
        }
        // int i = 0;
        // for (char c : t.toCharArray()) {
        //     if (s.charAt(i) == c && ++i == s.length()) {
        //         return true;
        //     }
        // }
        // return false;
        if (t.isEmpty() || t.length() < s.length()) {
            return false;
        }
        int sCtr = 0;
        int tCtr = 0;
        
        while (sCtr < s.length() && tCtr < t.length()) {
            if (s.charAt(sCtr) == t.charAt(tCtr)) {
                sCtr++;
            }
            tCtr++;
        }
        return (sCtr == s.length());
    }
}