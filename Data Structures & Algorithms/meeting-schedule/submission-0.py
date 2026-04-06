"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time O(NlogN), Space O(1)
        prev = -1
        intervals.sort(key = lambda i: i.start)
        for i in range(len(intervals)):
            if intervals[i].start < prev:
                return False
            else:
                prev = intervals[i].end
        return True