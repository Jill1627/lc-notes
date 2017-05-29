"""
LC 57 Insert interval
Solution: iterate all intervals, check start and end time overlaps

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        res = list()
        if intervals is None or len(intervals) == 0:
            res.append(newInterval)
            return res

        n = len(intervals)
        i = 0

        while i < n and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i].start <= newInterval.end:
            newStart = min(intervals[i].start, newInterval.start)
            newEnd = max(intervals[i].end, newInterval.end)
            newInterval = Interval(newStart, newEnd)
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
