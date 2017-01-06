"""
AKA：similar binary tree
问题：判断一个扭曲过的树是否相同 -- 相同条件为左右子树可互换过
思路：与same tree基本一致，附加可允许左右对称调换过
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
