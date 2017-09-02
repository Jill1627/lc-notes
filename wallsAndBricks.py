"""
LC 286 Walls and Gates
Idea: 2 solutions: use DFS backtracking, or BFS with a queue

DFS solution steps:
1. Initialize: loop through each spots, whenever sees a 0, enter dfs Helper
2. Within dfs helper, set up directions list for 4 directions
3. get new coordinates from directions, check for bounds and 1 condition: new cooridnates's value greater than old value + 1 (there is room to reduce to get minimal)
4. update value, enter further level

BFS solution steps:
1. Initialize a queue, add all 0's index pairs to queue
2. loop through all elements within queue
"""

"""Solution 1: DFS backtracking """
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])

        for i in xrange(n):
            for j in xrange(m):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, n, m)

    def dfs(self, rooms, i, j, n, m):
        # loop through each of the four directions
        directions = [0, 1, 0, -1, 0]
        for d in xrange(4):
            x = i + directions[d] #(0, 1, 0, -1)
            y = j + directions[d + 1] #(1, 0, -1, 0)
            if x >= 0 and x < n and y >= 0 and y < m and rooms[x][y] > rooms[i][j] + 1:
                # update with a lower value
                rooms[x][y] = rooms[i][j] + 1
                self.dfs(rooms, x, y, n, m)

"""Solution 2: BFS queue """
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0 or len(rooms[0]) == 0: return
        # add all gates to the queue
        queue = deque()
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        # bfs
        directions = [0, 1, 0, -1, 0]
        while queue:
            top = queue.popleft()
            i = top[0]
            j = top[1]
            for d in xrange(len(directions) - 1):
                x = i + directions[d]
                y = j + directions[d + 1]
                if x >= 0 and x < len(rooms) and y >= 0 and y < len(rooms[0]) and rooms[x][y] > rooms[i][j] + 1:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append([x, y])
