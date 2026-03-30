class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        answer = 0

        for r in range(len(s)):
            curr = s[r]
            if curr not in seen:
                seen[curr] = r
            else:
                l = max(seen[curr] + 1, l)
                seen[curr] = r
            answer = max(answer, r-l + 1)


        return answer