"""
LC 57 Insert interval
Solution: iterate all intervals, check start and end time overlaps

Idea: similar to merge interval, keep track of newStart and newEnd to create a merged interval

Steps:
1. Loop through each interval within intervals
2. Into 2 parts, leftPart is all the intervals that ends before new interval; rightPart is all intervals starts later than new interval -> no overlapping
3. In the middle, merge all intervals into one new interval by updating newStart to the earliest, and newEnd to the latest
4. Concatenate the res list

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
        newStart = newInterval.start
        newEnd = newInterval.end
        leftPart = list()
        rightPart = list()

        for inv in intervals:
            if inv.end < newStart:
                leftPart.append(inv)
            elif inv.start > newEnd:
                rightPart.append(inv)
            else: # merge
                newStart = min(newStart, inv.start)
                newEnd = max(newEnd, inv.end)
        return leftPart + [Interval(newStart, newEnd)] + rightPart


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
        # add all intervals ending before the start of new interval to res
        while i < n and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        # merge all overlapping intervals with new interval to res
        while i < n and intervals[i].start <= newInterval.end:
            newStart = min(intervals[i].start, newInterval.start)
            newEnd = max(intervals[i].end, newInterval.end)
            newInterval = Interval(newStart, newEnd)
            i += 1
        res.append(newInterval)
        # add all intervals starting after the end of new interval to res
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
