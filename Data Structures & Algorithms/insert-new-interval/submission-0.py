class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time O(N), Space O(N)
        res = [newInterval]
        for st, en in intervals:
            a, b = res[-1]
            if b < st:
                res.append([st, en])
            elif a > en:
                res.pop()
                res.append([st, en])
                res.append([a, b])
            else:
                res.pop()
                res.append([min(st, a), max(en, b)])
        return res