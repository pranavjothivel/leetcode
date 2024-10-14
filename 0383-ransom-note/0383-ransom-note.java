class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (magazine == null || magazine.isEmpty()) {
            return false;
        }
        HashMap<Character, Integer> ransomNoteLetters = new HashMap<>();
        HashMap<Character, Integer> magazineLetters = new HashMap<>();

        for (int i = 0; i < ransomNote.length(); i++) {
            char c = ransomNote.charAt(i);
            ransomNoteLetters.put(c, ransomNoteLetters.getOrDefault(c ,0) + 1);
        }
        for (int i = 0; i < magazine.length(); i++) {
            char c = magazine.charAt(i);
            magazineLetters.put(c, magazineLetters.getOrDefault(c ,0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : ransomNoteLetters.entrySet()) {
            Character key = entry.getKey();
            int value = entry.getValue();
            if (value > magazineLetters.getOrDefault(key, 0)) {
                return false;
            }
        }
        return true;
    }   
}