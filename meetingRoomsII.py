"""
LC 253 Meeting rooms II - return number of meeting rooms needed
Idea:
sort start times and end times of each interval separately
keep track of available room and number of rooms
"""

"""
Solution: sort intervals by start time, use a min heap to keep track of all meeting rooms in use
See in-line comments
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import operator

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or len(intervals) == 0: return 0

        # initialize
        intervals.sort(key = operator.attrgetter("start"))

        roomsInUse = list() # implement using priorityQueue - Python data structure heapQ
        heapq.heappush(roomsInUse, (intervals[0].end, intervals[0]))

        # loop through each interval by start time
        for i in xrange(1, len(intervals)):
            interval = heapq.heappop(roomsInUse)[1] # pops the meeting that ends earliest
            if intervals[i].start >= interval.end:
                interval.end = intervals[i].end # no conflict, merge the two intervals
            else:
                heapq.heappush(roomsInUse, (intervals[i].end, intervals[i]))

            heapq.heappush(roomsInUse, (interval.end, interval))

        return len(roomsInUse)




"""
Solution: using 2 array starts and ends, sort
Steps:
1. Initialize: array of start times, array of end times, index of start time, index of end time, number of rooms being used simultaneously, number of rooms available to be used (previously acquired, but now released to be use)
2. Sort start times, and sort end times
3. Use start pointer and end pointer for each array, while s not reach the end of start array

"""

""" Solution without using availableRoom variable """
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or len(intervals) == 0: return 0
        starts = list()
        ends = list()
        s = e = 0
        numRooms = 0

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        for s in xrange(len(starts)):
            if starts[s] < ends[e]:
                numRooms += 1
            else:
                e += 1
        return numRooms


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or len(intervals) == 0: return 0
        starts = list()
        ends = list()
        s = e = 0
        numRooms = available = 0

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return numRooms
