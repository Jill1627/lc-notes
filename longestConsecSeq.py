# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    longest = 0
    def longestConsecutive(self, root):
        if root is None:
            return self.longest
        self.dfs_helper(root, 0, root.val)
        return self.longest
    def dfs_helper(self, node, count, target):
        if node is None:
            return
        if node.val == target:
            count += 1
        else:
            count = 1
        self.longest = max(self.longest, count)
        self.dfs_helper(node.left, count, node.val + 1)
        self.dfs_helper(node.right, count, node.val + 1)
