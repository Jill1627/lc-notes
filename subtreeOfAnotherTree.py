"""
LC 572 Subtree of another tree

Idea: recusion with a helper method of isSameTree

Steps:
1. if s does not exist, False;
2. Base case: if s and t isSameTree -> True
3. Recurrence: check t is s's left subtree or right subtree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False

        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
