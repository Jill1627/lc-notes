# LC 339 Nested List Weight Sum
"""
Recursive: use a helper method which takes depth as parameter
Iterative: Queue + BFS
"""

""" Recursive """
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0
        depth = 1
        return self.depthHelper(nestedList, depth)

    def depthHelper(self, nestedList, depth):
        res = 0
        for elem in nestedList:
            if elem.isInteger():
                res += elem.getInteger() * depth
            else:
                res += self.depthHelper(elem.getList(), depth + 1)
        return res

""" Iterative: use queue + level order traversal """
from collections import deque
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        queue = deque(nestedList)
        res = 0
        depth = 1
        while queue:
            size = len(queue)
            for i in xrange(size):
                elem = queue.popleft()
                if elem.isInteger():
                    res += elem.getInteger() * depth
                else:
                    for ni in elem.getList():
                        queue.append(ni)
            depth += 1
        return res

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
