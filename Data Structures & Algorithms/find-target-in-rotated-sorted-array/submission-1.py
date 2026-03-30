class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # num[m] is in the "left" portion
            if nums[l] <= nums[m]:

                if nums[l] > target or target > nums[m]:
                    # look through the "right" portion, as if the target is not in
                    # the left portion, it must be in the "right" portion
                    l = m +1

                    # now perform binary search
                else:
                    # target is in the left portion, perform binary search
                    r = m - 1

            # m is in the "right" portion
            else:
                


                if nums[r] < target or target < nums[m]:
                    # the target is in the "left" portion
                    r = m - 1
                else:
                    # the target is in the "right" portion
                    l = l + 1
        return -1