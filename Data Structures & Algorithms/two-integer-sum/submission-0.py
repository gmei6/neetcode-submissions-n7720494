class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps number → index
        for index, element in enumerate(nums):
            complement = target - element
            if complement in seen:   # if we’ve seen the number we need
                return [seen[complement], index]
            seen[element] = index    # store this element for future checks