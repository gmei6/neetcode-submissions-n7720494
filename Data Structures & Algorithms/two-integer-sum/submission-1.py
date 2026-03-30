class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, element in enumerate(nums):
            complement = target - element
            if complement in seen:
                return [seen[complement], i]
            seen[element] = i