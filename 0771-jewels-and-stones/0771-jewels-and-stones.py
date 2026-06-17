from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set=set(jewels)
        stones_counter = Counter(stones)
        ans=0

        for j in jewels_set:
            if j in stones_counter.keys():
                ans = ans + stones_counter[j]
        return ans