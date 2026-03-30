class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for element in nums:
            if element in map:
                return True
            else:
                map[element] = element
        return False