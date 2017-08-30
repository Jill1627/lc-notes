"""
LC.366 Find Leaves of Binary Tree
Strategy: use a helper method to calculate height of node, and along the way, update result
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        if not root:
            return res
        self.height(root, res)
        return res
    def height(self, root, res):
        if root is None:
            return 0
        height = 1 + max(self.height(root.left, res), self.height(root.right, res))
        while len(res) < height:
            res.append(list())
        res[height - 1].append(root.val)
        return height
