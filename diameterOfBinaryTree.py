"""
LC 543 Diameter of binary tree - same as longest path from any node to any node

Idea: recursion to find maxDepth of left subtree and right subtree, constantly update maxDiameter
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        self.res = 0
        # use a inner class to avoid playing with global variable
        def maxDepth(root):
            if root is None:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.res = max(self.res, left + right + 1)
            return 1 + max(left, right)

        maxDepth(root)
        return self.res - 1 # diameter is one node less than longest path
