class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longest = 0

        for number in hashset:
            if number - 1 not in hashset:
                next_num = number + 1
                temp = 1
                while next_num in hashset:
                    temp += 1
                    next_num += 1
                longest = max(longest, temp)
        
        return longest
            
            