"""
LC 257
Print out all the paths from root to leaf of binary tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = list()
        if root is None: return res
        self.dfs(root, res, "")
        return res

    def dfs(self, node, res, path):
        if node.left is None and node.right is None:
            res.append(path + str(node.val))
            return
        if node.left:
            self.dfs(node.left, res, path + str(node.val) + "->")
        if node.right:
            self.dfs(node.right, res, path + str(node.val) + "->")
