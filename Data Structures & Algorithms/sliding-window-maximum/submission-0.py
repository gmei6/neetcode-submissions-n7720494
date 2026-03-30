class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ans = []
        for r in range(k-1, len(nums)):
            # Find the max
            temp = max(nums[l:r+1])
            print(nums[l:r+1])

            # Add max to ans
            ans.append(temp)
            l += 1
        return ans