"""
LC.277 Find the celebrity
Strategy: two pass
1 pass: identify a celebrity candidate
2 pass: verify the celebrity candidate
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # two pass
        # 1. find the celebrity candidate
        celebrity = 0
        for i in xrange(1, n):
            if not knows(i, celebrity):
                celebrity = i

        # 2. Verify celebrity satisfy requirements
        for i in xrange(n):
            if i != celebrity and (knows(celebrity, i) or not knows(i, celebrity)):
                return -1
        return celebrity
