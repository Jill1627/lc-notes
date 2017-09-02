"""
LC 221 Maximal square

Idea: DP
function definition: dp[i][j] = max square side length ending at matrix[i][j]

Steps:
1. initialize a 2d matrix dp[m + 1][n + 1], a variable maxLen max length of square side
2. loop, whenever encountering a '1', dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1, as the three fields takes care of horizontal, vertical, and diagonal length
3. update maxLen, result just square the maxLen to get max square size

Follow up:
Improve space complexity
"""

"""O(mn) time, O(mn) space"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for i in xrange(m + 1)]
        maxLen = 0

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen * maxLen

"""O(mn) time, O(n) space"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        maxLen = 0
        prev = 0

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(prev, dp[j - 1], dp[j]) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxLen * maxLen
