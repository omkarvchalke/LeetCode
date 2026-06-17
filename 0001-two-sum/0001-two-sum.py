class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={} #hashmap of {value:index} from list nums
        for i in range(len(nums)): #adding last index of specific value in hashmap
            h[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i] #y is the 2nd number from nums 

            if y in h and h[y]!=i:
                return [i,h[y]]


        