"""
问题：判断一棵树是否高度平衡（任何node的左右子树高度差不超过1）
思路：recursion每一个子节的左右子树高度差，用-1标记超过
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
        return self.maxHeight(root) != -1

    def maxHeight(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftH = self.maxHeight(root.left)
        rightH = self.maxHeight(root.right)
        if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
            return -1
        return max(leftH, rightH) + 1
