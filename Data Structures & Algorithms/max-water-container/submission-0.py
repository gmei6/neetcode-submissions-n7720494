class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            minHeight = min(heights[left], heights[right])
            tempWater = (right - left) * minHeight
            
            if maxWater < tempWater:
                maxWater = tempWater

            if heights[left] - heights[right] > 0:
                right = right - 1
            else:
                left = left + 1

        return maxWater
        