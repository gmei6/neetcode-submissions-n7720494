class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            map = {}
            for char in s:
                if char not in map:
                    map[char] = 1
                else:
                    map[char] = map[char] + 1
            for char in t:
                if char in map:
                    map[char] = map[char] - 1
        if any(v != 0 for v in map.values()):
            return False
        else:
            return True

        