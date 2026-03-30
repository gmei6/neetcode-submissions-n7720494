from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        duplicates = [item for item, count in counts.items() if count > 1]

        return duplicates[0]