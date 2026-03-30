class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for i, element in enumerate(numbers):
            complement = target - element
            print("Index: ", i)
            print("element:", element)
            print("complement: ", complement)
            if (element in map):
                return [map[element] + 1,i + 1]
            else:
                map[complement] = i
                print("map", map)
                print("")