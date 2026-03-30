class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for element in nums:
            if element not in map:
                map[element] = 1
            else:
                map[element] += 1
        
        output = []
        print(map)

        for i in range(k):
            greatest_key = max(map, key=map.get)
            print("This is the greatest key", greatest_key)
            output.append(greatest_key)
            del map[greatest_key]

        return output
