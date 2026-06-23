class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        h = 0
        w = 0

        while left < right:
            w = right - left
            h = min(height[left],height[right])
            area=w*h
            max_area= max(max_area,area)
            
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
               
            
        return max_area