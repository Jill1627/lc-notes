"""
LC 69 Sqrt(x)
Binary search
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x

        start = 1
        end = x / 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
