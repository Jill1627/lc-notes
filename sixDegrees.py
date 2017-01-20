"""
sixDegrees is a typical BFS in undirected graph problem
思路：用一个Map来存visited node 和 degree，用一个queue来存等待访问的node
hashmap来存储每个node对应的degree（相对于s）
"""

from collections import deque

class UndirectedGraphNode:
    def __init__(self, value):
        self.label = value
        self.neighbors = list()

class Solution:
    def sixDegrees(self, graph, s, t):
        if s == t:
            return 0

        visited = dict()
        queue = deque()

        queue.append(s)
        visited[s] = 0

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    continue
                if neighbor is t: # neighbor == t may also work here
                    return visited[curr] + 1
                queue.append(neighbor)
                visited[neighbor] = visited[curr] + 1
        return -1
