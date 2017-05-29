""" LC 56 Merge Intervals """

"""
Strategy:
1. Sort all intervals by start time
2. Iterate through sorted list, if latter start prior to curr end, Merge
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return intervals
        sortedIntl = sorted(intervals, key = lambda i : i.start)
        result = list()
        currStart = sortedIntl[0].start
        currEnd = sortedIntl[0].end
        merged = sortedIntl[0]
        for i in range(1, len(sortedIntl)):
            if sortedIntl[i].start <= currEnd:
                currEnd = max(sortedIntl[i].end, currEnd)
                merged = Interval(currStart, currEnd)
            else:
                result.append(merged)
                currStart = max(sortedIntl[i].start, currStart)
                currEnd = max(sortedIntl[i].end, currEnd)
                merged = Interval(currStart, currEnd)
        result.append(merged)
        return result
