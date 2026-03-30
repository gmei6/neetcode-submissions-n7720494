class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        dic = {}

        for i in range(0, len(s1)):
            dic[s1[i]] = dic.get(s1[i], 0) + 1

        temp = {}
        for r in range(0, len(s2)):
            temp[s2[r]] = temp.get(s2[r], 0) + 1

            # if the char not in s1
            if s2[r] not in dic:
                l = r + 1
                temp = {}
            
            # if lengths are the same but it's not a permutation
            if r - l + 1 == len(s1) and dic != temp:
                temp[s2[l]] -= 1
                if temp[s2[l]] == 0:
                    del temp[s2[l]]

                l += 1

            
            if dic == temp:
                return True
        return False