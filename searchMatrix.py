"""
问题：给一个2D array matrix，从左至右sorted，从上到下sorted，问target value是否存在
思路：二分法
Key: 找到mid所在的x，y位置即可
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])
        if matrix is None or n == 0:
            return -1
        if matrix[0] is None or m == 0:
            return -1

        start = 0
        end = n * m - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid / m][mid % m] == target:
                return True
            if matrix[mid / m][mid % m] > target:
                end = mid
            else:
                start = mid
        if matrix[start / m][start % m] == target or matrix[end / m][end % m] == target:
            return True
        else:
            return False
