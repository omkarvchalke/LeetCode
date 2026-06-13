class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        min_len = min(len(word1),len(word2))

        for i in range(min_len):
            ans = ans + word1[i] + word2[i]
        
        if len(word1)>len(word2):
            ans = ans + word1[min_len:]
        else:
            ans = ans + word2[min_len:]
        return ans