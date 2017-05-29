"""
LC.254 Factor Combinations

"""

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = list()
        self.helper(res, [], 2, n)
        return res

    def helper(self, res, level, start, n):
        if n <= 1:
            if len(level) > 1:
                res.append(list(level))
            return
        for i in xrange(start, n + 1):
            if n % i == 0:
                level.append(i)
                self.helper(res, level, i, n / i)
                level.pop()
