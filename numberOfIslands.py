# LC 200 number of islands
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
