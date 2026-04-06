class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time O(N), Space O(1)
        res = 0
        if len(intervals) == 0:
            return res
        intervals.sort(key=lambda i: i[1])
        ca, cb = intervals[0]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a >= cb:
                ca, cb = a, b
            else:
                res += 1
        return res