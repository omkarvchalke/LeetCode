"""class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans=[]

        for i in range (n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i]==nums[i-1]:
                continue
             
            low,high=i+1, n-1
            while low<high:
                if nums[i]+nums[low]+nums[high]==0:
                    ans.append([nums[i],nums[low],nums[high]])
                    low=low+1
                    high=high-1
                    while low < high and nums[low]==nums[low-1]:
                        low = low+1
                    while low < high and nums[high]==nums[high+1]:
                        high+=1 
                elif nums[i]+nums[low]+nums[high]>0:
                    low = low+1
                else:
                    high = high-1
        return ans   """

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res