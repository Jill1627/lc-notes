"""LC 515 Find largest value on each tree row"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        if root is None:
            return res
        q = deque()
        q.append(root)
        while q:
            levelSize = len(q)
            levelMax = -sys.maxint
            for i in xrange(levelSize):
                node = q.popleft()
                levelMax = max(node.val, levelMax)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelMax)
        return res
