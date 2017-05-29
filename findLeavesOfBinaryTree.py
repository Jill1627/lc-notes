"""
LC.366 Find Leaves of Binary Tree
Strategy
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
        if root is None:
            return root
        res = list()
        self.helper(root, res)
        return res
    # Helper function returns the height of a node - if leaf, then 0
    def height(self, node, res):
        if node is None:
            return -1
        level = 1 + max(self.height(node.left, res), self.height(node.right, res))
        # add a level to the res if res does not contain all the levels
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level
