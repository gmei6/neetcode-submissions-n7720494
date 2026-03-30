class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sAlph = [0] * 26
        tAlph = [0] * 26

        for char in s:
            sAlph[ord(char) - ord('a')] += 1

        for char in t:
            tAlph[ord(char) - ord('a')] += 1

        if sAlph == tAlph:
            return True
        else:
            return False