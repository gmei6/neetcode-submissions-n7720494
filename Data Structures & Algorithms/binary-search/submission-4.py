class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (right + left)//2
        midValue = nums[mid]

        counter = 0

        while counter <= len(nums)//2:
            if midValue > target:
                right = mid - 1
                mid = (right + left)//2
                midValue = nums[mid]
                counter += 1
            else:
                left = mid + 1
                mid = (right + left)//2
                midValue = nums[mid]
                counter += 1
        if midValue == target:
            return mid
        else:
            return -1
