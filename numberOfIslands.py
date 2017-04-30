# LC 200 number of islands

""" DFS """
class Solution(object):
    dirs = [[0,1], [0,-1], [1, 0], [-1, 0]]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        n = len(grid)
        if n == 0: return count
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '*'
                    self.dfs(grid, i, j)
        return count
    def dfs(self, grid, i, j):
        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1': continue
            grid[x][y] = '*'
            self.dfs(grid, x, y)

""" DFS II straight forward """
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

""" Union Find """
