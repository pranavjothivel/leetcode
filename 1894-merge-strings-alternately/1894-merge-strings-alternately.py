class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1_list = list(word1)
        word2_list = list(word2) 

        while word1_list and word2_list: 
            result += word1_list.pop(0) 
            result += word2_list.pop(0) 

        result += ''.join(word1_list)
        result += ''.join(word2_list)
        return result