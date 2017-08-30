"""
LC 200 Number of islands
Idea: dfs + once visiting a spot, mark as 0 to eliminate repetitive visit
Steps:
1. Loop 2d matrix n * m
2. Whenever encounter a '1', enters dfs and increment numberOfIslands (result)
3. dfs helper method (recusions)
    - Base case: when index reaches boundary or current one is not '1', return
    - Mark current [i][j] spot as '0' - sink it to avoid repetitive visiting
    - dfs up, down, left, right 4 directions
"""


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

""" Union Find with syntactical errors """
class Solution(object):
    # define an inner class UnionFind
    class UnionFind(object):

        def __init__(self, grid, n, m):
            self.grid = grid
            self.n = n
            self.m = m
            self.count = 0
            rep = [[i] for i in range(n * m)]
            count = 0
            for i in xrange(n):
                for j in xrange(m):
                    if grid[i][j] == '1':
                        count += 1
        # find with path compression
        def find(self, n):
            if self.rep[n] == n:
                return n
            sel.rep = self.find(rep[n])
            self.rep[n] = rep
            return rep

        def union(self, p, q):
            prep = self.find(p)
            qrep = self.find(q)
            if prep == qrep: return
            if prep < qrep:
                rep[prep] = qrep
            else:
                rep[qrep] = prep
            count -= 1



    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        uf = self.UnionFind(grid, n, m)
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == '1':
                    # up
                    p = i * n + j
                    if i > 0 and grid[i - 1][j] == '1':
                        q = p - n
                        uf.union(p, q)
                    # down
                    if i < n - 1 and grid[i + 1][j] == '1':
                        q = p + n
                        uf.union(p, q)
                    # left
                    if j > 0 and grid[i][j - 1] == '1':
                        q = p - 1
                        uf.union(p, q)
                    # right
                    if j < m - 1 and grid[i][j + 1] == '1':
                        q = p + 1
                        uf.union(p, q)
