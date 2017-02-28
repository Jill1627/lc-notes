# LC230

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

""" DFS inorder recursive """

class Solution(object):
    target = 0
    count = 0
    def kthSmallest(self, root, k):
        self.count = k
        self.inorder(root)
        return self.number
    def inorder(self, node):
        if node.left is not None: self.inorder(node.left)
        self.count -= 1
        if self.count == 0:
            self.number = node.val
            return
        if node.right is not None: self.inorder(node.right)



""" DFS recursion """
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.countNode(root.left); # number of nodes on left subtree
        if k <= count:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - count) # find the k - 1 - count nodes in the right subtree

    def countNodes(self, n):
        if n is None: return 0
        return 1 + self.countNodes(n.left) + self.countNodes(n.right)
