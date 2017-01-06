"""
问题：判断一棵树是否对称
思路：使用辅助程序判断左子树和右子树是否成mirror关系
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        if not a and not b:
            return True
        if a and b:
            left = self.isTweakedIdentical(a.left, b.left) or self.isTweakedIdentical(a.left, b.right)
            right = self.isTweakedIdentical(a.right, b.right) or self.isTweakedIdentical(a.right, b.left)
            return a.val == b.val and left and right
        return False
