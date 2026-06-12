class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       # 2 pointer approach : O(n)
        left = 0
        right = len(nums)-1
        res = []
        while left <= right :
            if abs(nums[left])> abs(nums[right]):
                res.append(nums[left]**2)
                left = left +1
            else:
                res.append(nums[right]**2)
                right = right -1
        res.reverse()
        return res

        
        