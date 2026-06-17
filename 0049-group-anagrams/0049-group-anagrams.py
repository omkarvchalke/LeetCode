from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            count = [0]*26 #making list with 26 0's to count characters -> 'abc' = [1,1,1,0,0,.....]
            for ch in s:
                count[ord(ch)-ord('a')] +=1 #ord() gives ASCII values -> for 'd'

            key = tuple(count) #making tuple because it is hashable
            anagram_dict[key].append(s)
        return list(anagram_dict.values())

            
