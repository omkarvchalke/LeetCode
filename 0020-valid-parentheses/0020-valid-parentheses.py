class Solution:
    def isValid(self, s: str) -> bool:
        d={"}":"{",")":"(","]":"["}
        stk=[]
        for br in s:
            if br not in d:
                stk.append(br)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != d[br]:
                        return False
        return not stk

