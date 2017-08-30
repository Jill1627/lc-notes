# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
LC 252 Meeting rooms
Idea: sort all meetings by start time, loop through, once there is cross, return False
Till the end, return True
"""


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals is None or len(intervals) == 0 : return True

        # sort intervals
        sortedIntervals = sorted(intervals, key = lambda i : i.start)

        # check each interval within sortedIntervals, whenever cross, return False
        for i in xrange(1, len(sortedIntervals)):
            if sortedIntervals[i].start < sortedIntervals[i - 1].end:
                return False
        return True
