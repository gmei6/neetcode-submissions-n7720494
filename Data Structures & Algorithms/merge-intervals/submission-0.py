from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.merge_sort_merge(intervals)
    
    def merge_sort_merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals[:]  

        mid = n // 2
        left  = self.merge_sort_merge(intervals[:mid])
        right = self.merge_sort_merge(intervals[mid:])

        return self._merge_two_merged_lists(left, right)
    
    def _merge_two_merged_lists(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i = j = 0
        out: List[List[int]] = []

        def push(s: int, e: int) -> None:
            if not out or s > out[-1][1]:
                out.append([s, e])
            else:
                out[-1][1] = max(out[-1][1], e)

        while i < len(a) and j < len(b):
            if a[i][0] <= b[j][0]:
                push(a[i][0], a[i][1])
                i += 1
            else:
                push(b[j][0], b[j][1])
                j += 1

        while i < len(a):
            push(a[i][0], a[i][1])
            i += 1

        while j < len(b):
            push(b[j][0], b[j][1])
            j += 1

        return out
