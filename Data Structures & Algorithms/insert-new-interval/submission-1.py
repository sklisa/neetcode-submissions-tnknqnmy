class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time O(N), Space O(N)                                                                                                                                                                             )
        res = []
        na, nb = newInterval
        for i in range(len(intervals)):
            a, b = intervals[i]
            if nb < a:
                res.append([na, nb])
                return res + intervals[i:]
            elif na > b:
                res.append([a, b])
            else:
                na, nb = min(na, a), max(nb, b)
        res.append([na, nb])
        return res