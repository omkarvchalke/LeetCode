class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close_num = nums[0]
        for x in nums:
            if abs(x)<abs(close_num):
                close_num=x
        if close_num < 0 and abs(close_num) in nums:
            return abs(close_num)
        else:
            return close_num