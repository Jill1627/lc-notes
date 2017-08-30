"""
LC311 Sparse matrix multiplication
Idea:
resulting matrix size is rowA * colB
Insert non-zero checks

Loop through each element of A, encountering a non-zero element -> start loop through B, row[j] is fixed for B, only loop through all cols
increment res for corresponding row and col
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowA = len(A)
        colA = len(A[0])
        rowB = colA
        colB = len(B[0])
        res = [[0] * colB for i in xrange(rowA)]
        for i in xrange(rowA):
            for j in xrange(colA):
                if A[i][j] != 0:
                    for k in xrange(colB):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j] * B[j][k]
        return res
