#270

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Iterative
"""
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            closest = root.val if abs(root.val - target) < abs(closest - target) else closest
            root = root.left if target < root.val else root.right
        return closest



"""
Recursive
"""
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        child = root.left if target < a else root.right
        if not child: return a
        b = self.closestValue(child, target)
        res = a if abs(target - a) < abs(target - b) else b
        return res
