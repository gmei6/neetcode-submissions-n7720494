import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        items = len(piles)
        time_available_per_item = h // items
        max_bannanas = max(piles)
        right = math.ceil(max_bannanas / time_available_per_item)

        #now do binary search from [0,right]
        left = 1
        middle = 0

        while left <= right:

            middle = (left + right) // 2
            
            time_taken = 0 
            for i in range (0, len(piles)):
                time_taken += math.ceil(piles[i] / middle)
                if time_taken > h:
                    break
            if time_taken > h:
                left = middle + 1
            else: # covers both < h and == h
                right = middle - 1
        return left