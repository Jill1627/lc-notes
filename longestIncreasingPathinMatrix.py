""" 有bug """


class Solution(object):
    directions = [[0,1], [1,0],[0,-1],[-1,0]]
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        if n == 0: return 0
        cache = n * [m * [0]]
        longest = 1
        for i in range(n):
            for j in range(m):
                pathLen = self.dfs(matrix, i, j, n, m, cache)
                longest = max(longest, pathLen)
        return longest

    def dfs(self, matrix, i, j, n, m, cache):
        if cache[i][j] != 0: return cache[i][j]
        longest = 1
        for dir in self.directions:
            x = i + dir[0]
            y = j + dir[1]
            if x < 0 or x >= n or y < 0 or y >= m or matrix[x][y] <= matrix[i][j]: continue
            pathLen = 1 + self.dfs(matrix, x, y, n, m, cache)
            longest = max(longest, pathLen)
        cache[i][j] = longest
        return longest
