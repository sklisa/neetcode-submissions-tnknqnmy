class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time O(NlogN), Space O(N)
        res = []
        if len(intervals) == 0:
            return res
        intervals.sort()
        ca, cb = intervals[0]
        for a, b in intervals:
            if cb < a:
                res.append([ca, cb])
                ca, cb = a, b
            else:
                cb = max(cb, b)
        res.append([ca, cb])
        return res