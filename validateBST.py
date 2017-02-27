"""
思路：bfs for inorder traversal 录入ascending array，一旦前面>=后面，false
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root, -sys.maxint, sys.maxint)

    def helper(self, root, lo, hi):
        if root is None:
            return True
        if root.val >= hi or root.val <= lo:
            return False
        left = self.helper(root.left, lo, root.val)
        right = self.helper(root.right, root.val, hi)
        return left and right
