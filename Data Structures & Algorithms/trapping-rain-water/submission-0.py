class Solution:
    def trap(self, height: List[int]) -> int:
        # first we remove all edges that cannot contain water

        left = 0
        right = len(height) - 1
        water = 0

        maxLeft = height[left]
        maxRight = height[right]

        while right - left != 0:
            if maxLeft <= maxRight:
                left += 1
                water += max(0, maxLeft - height[left])
                if maxLeft < height[left]:
                    maxLeft = height[left]
            else:
                right -= 1
                water += max(0, maxRight - height[right])
                if maxRight < height[right]:
                    maxRight = height[right]
                
            
        return water
        