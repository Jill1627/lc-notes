"""
LC 598. Range Addition II
Given a 2D matrix m * n, given another 2D matrix ops, for each op in ops is a list [a, b], a is a range 0 ~ a, b is a range 0 ~ b, to increment matrix m * n in that range by 1

return: the number of maximum value in the matrix
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        if len(ops) == 0:
            return m * n
        row = m
        col = n
        for incre in ops:
            row = min(row, incre[0])
            col = min(col, incre[1])
        return row * col
