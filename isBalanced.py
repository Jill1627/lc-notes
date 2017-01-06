"""
问题：看是否是平衡二叉树
思路：recursion 看左右，一旦左或右不平衡了，就用-1标记不平衡
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if not root:
            return 0
        leftD = self.maxDepth(root.left)
        rightD = self.maxDepth(root.right)
        if leftD == -1 or rightD == -1 or abs(leftD - rightD) > 1:
            return -1
        return max(leftD, rightD) + 1
