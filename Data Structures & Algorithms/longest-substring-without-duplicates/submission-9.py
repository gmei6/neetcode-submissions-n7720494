class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        answer = 0

        while r < len(s):
            curr = s[r]
            print("this is s[r]: ", curr)
            if curr not in seen:
                # print("s[r] is not in seen")
                seen[curr] = r
                r += 1
                # print("This is seen: ", seen)
                # print("This is the answer: ", answer)
            else:
                # print("s[r] is in seen")
                # print("this is l and r", l, r)
                
                l = max(seen[curr] + 1, l)
                seen[curr] = r
                r += 1
                # print("This is seen: ", seen)
                # print("This is the answer: ", answer)
            answer = max(answer, r-l)
            # print("")


        return answer