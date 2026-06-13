class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       #Two Pointer
        i = 0
        j = 0
        if s == '':return True
        if len(s)>len(t):return False

        for j in range(len(t)):
            if t[j]==s[i]:
                if i == len(s)-1:
                    return True
                i=i+1
        return False

        return i == len(s)