"""
LC. 112 Path Sum
See if can Find a root to leaf path that sum up to target
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
""" My own solution """

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.val == target and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)



class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        if left or right:
            return True
        else:
            return False
