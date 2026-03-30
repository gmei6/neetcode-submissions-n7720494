class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(0, len(heights)):
            # calculate the area of a column at position i
            leftIndex = i
            rightIndex = i
            while leftIndex - 1 >= 0 and heights[leftIndex-1] >= heights[i]:
                leftIndex -= 1
            while rightIndex + 1 < len(heights) and heights[rightIndex+1] >= heights[i]:
                rightIndex += 1
            currArea = (rightIndex - leftIndex + 1) * heights[i]
            if currArea > maxArea:
                maxArea = currArea
        return maxArea