"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    node = None
    sum = 0
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    def findSubtree(self, root):
        if root is None:
            return root
        self.recur_helper(root)
        return self.node
    def recur_helper(self, root):
        if root is None:
            return 0 # sum
        left_sum = self.recur_helper(root.left)
        right_sum = self.recur_helper(root.right)
        sub_sum = left_sum + right_sum + root.val
        if self.node is None or sub_sum < self.sum:
            self.node = root
            self.sum = sub_sum
        return sub_sum
