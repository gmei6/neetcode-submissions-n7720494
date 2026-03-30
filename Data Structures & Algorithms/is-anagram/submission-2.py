class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sAlph = [0] * 26
        tAlph = [0] * 26

        for i in range(len(s)):
            sAlph[ord(s[i]) - ord('a')] += 1
            tAlph[ord(t[i]) - ord('a')] += 1
            

        if sAlph == tAlph:
            return True
        else:
            return False