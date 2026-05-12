"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if intervals:
            last_interval = intervals[0]
            for i in intervals[1:]:
                if last_interval.end > i.start:
                    return False
                else:
                    last_interval.end = max(last_interval.end,i.end)
        
        return True