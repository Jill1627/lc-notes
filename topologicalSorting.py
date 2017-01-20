"""
问题：输出有向图的拓扑排序
思路：BFS, queue, hashmap
"""

from collections import deque()

class Solution(object):
    def topologicalSorting(self, graph):
        result = list()
        if graph is None or len(graph) == 0:
            return result

        degreeMap = dict()
        queue = deque()
        """
        Step 1: 将所有点加入degreeMap，node : indegree
        """
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in degreeMap:
                    degreeMap[neighbor] = degreeMap[neighbor] + 1
                else:
                    degreeMap[neighbor] = 1
        """
        Step 2: 将所有indegree = 0的点加入答案，并且加入queue, as starting nodes
        """
        for node in graph:
            if node not in degreeMap:
                queue.append(node)
                result.append(node)
        """
        Step 3: BFS queue中所有点，没看一次就in degree就-1，等到为0时，就ready了
        """
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                degreeMap[neighbor] = degreeMap[neighbor] - 1
                if degreeMap[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
        return result
