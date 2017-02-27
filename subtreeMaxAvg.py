"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    average = 0;
    node = None
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        # need subtree sum, and size
        if not root:
            return root
        self.recur_helper(root)
        return self.node
    def recur_helper(self, node):
        if node is None:
            return 0, 0
        leftSum, leftSize = self.recur_helper(node.left)
        rightSum, rightSize = self.recur_helper(node.right)
        totalSum = leftSum + rightSum + node.val
        totalSize = leftSize + rightSize + 1
        if node is None or totalSum * 1.0 / totalSize > self.average:
            self.average = totalSum * 1.0 / totalSize
            self.node = node
        return totalSum, totalSize # return sum, size of current tree
