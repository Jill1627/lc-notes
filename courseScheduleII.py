"""
LC 210 Course Schedule II
Idea: Build a graph and do top sort
"""

# BFS
class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        # graph stores course with a set of prerequesites
        graph = {i: set() for i in xrange(numCourses)}
        # neigh stores prereq with a set of neighbors (outgoing edges)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in graph if not graph[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                graph[i].remove(node)
                if not graph[i]:
                    queue.append(i)
        return res if count == numCourses else []

# DFS
def findOrder(self, numCourses, prerequisites):
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in xrange(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []
