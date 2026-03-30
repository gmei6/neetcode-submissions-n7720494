class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for number in nums:
            #print("This is the list:", counter)
            if number in my_map:
                return True
            else:
                my_map[number] = number
        return False
        