"""
LC 274 H-index

Solution 1: sort - reverse loop, exit when citations[some pos] > i, h-index = some pos + 1

Solution 2: counting
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        sorted(citations)
        i = 0
        while (i < len(citations) and citations[len(citations) - 1 - i] > i ):
            i += 1
        return i

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        # construct papers array
        n = len(citations)
        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1 # Trick: if c is really high, replace it with n, it won't affect the H-index - max of H-index is n
        # get H-index
        k = n # starting from the highest index as candidate h-index
        count = papers[n] # number of paper that has highest citation
        while k > count:
            count += papers[k - 1]
            k -= 1
        return k
