""" LC 56 Merge Intervals """

"""
Strategy:
1. Sort all intervals by start time
2. Iterate through sorted, if latter start prior to curr end, Merge
3. Use currentStart and currentEnd variables to mark the interval under merging
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
            # curr interval overlap with previous merge interval
            if sortedIntl[i].start <= currEnd:
                currEnd = max(sortedIntl[i].end, currEnd)
                merged = Interval(currStart, currEnd)
            # curr interval does NOT overlap, start a new merged interval
            else:
                result.append(merged)
                currStart = sortedIntl[i].start
                currEnd = sortedIntl[i].end
                merged = Interval(currStart, currEnd)
        result.append(merged)
        return result
