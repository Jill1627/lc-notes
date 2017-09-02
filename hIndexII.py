"""
275 H-index II
Idea: binary search

"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        start = 0
        end = len(citations) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            # case: count of citations = number of papers have greater or equal citations than
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] < len(citations) - mid:
                end = mid
            else:
                start = mid
        if citations[end] >= len(citations) - end:
            return len(citations) - end
        else:
            return len(citations) - start
