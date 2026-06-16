class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        #Time : Space : O(n) -> we created a Set()
        #Optimal Solution with Space O(1) -> Floyd's Cycle Detection