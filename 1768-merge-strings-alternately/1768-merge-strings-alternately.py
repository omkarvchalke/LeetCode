class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        min_len = min(len(word1),len(word2))

        for i in range(min_len):
            ans.append(word1[i])
            ans.append(word2[i])
        
        if len(word1)>len(word2):
            ans.append(word1[min_len:])
        else:
            ans.append(word2[min_len:])
        return "".join(ans)

        #Time and Space O(m+n) -> appending string takes space