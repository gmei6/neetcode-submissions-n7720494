class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = []
        for number in nums:
            #print("This is the list:", counter)
            if number in counter:
                return True
            else:
                counter.append(number)
        return False
        