class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #FIXED SLIDING WINDOW
        n = len(nums)
        cur_sum = 0
        #step 1: building first window
        for i in range(k):
            cur_sum = cur_sum + nums[i]
        
        #avg of first window
        max_avg = cur_sum/k

        for i in range(k,n):
            cur_sum = cur_sum + nums[i]
            cur_sum = cur_sum - nums[i-k]

            avg = cur_sum/k
            max_avg = max(max_avg,avg)

        return max_avg
