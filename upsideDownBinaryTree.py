""" LC156 Binary Tree Upside Down """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Base case: if there is no root or root has no left child, nothing to upside down
        if not root or not root.left:
            return root
        # leftRoot is the candidate to become new root, after fixing its subtree unit
        # leftRoot now is a left child, after fixing, it becomes root
        leftRoot = self.upsideDownBinaryTree(root.left)
        # rightMost is supposed to be the right most TreeNode within the whole tree rooted at leftRoot
        rightMost = leftRoot
        while rightMost.right:
            rightMost = rightMost.right
        # process of fixing
        # connect original root's right child to be right most bottom node's left
        rightMost.left = root.right
        # connect original root's value (can't be root, should be a new node) to be right most bottom node's right child
        rightMost.right = TreeNode(root.val)
        # update the root
        root = leftRoot
        return root
