"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Time O(NlogN), Space O(N)
        res = 0
        intervals.sort(key = lambda i: i.start)
        heap = [] # endTime
        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            res = max(res, len(heap))
        return res