"""
LC 236 Lowest common ancestor of binary tree
Recur / going deep from root, encounter whichever first, mark as LCA
if both subtree returned, indicating each subtree contains one, return root
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == p or root == q:
            return root
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        if leftLCA and rightLCA:
            return root
        return leftLCA if leftLCA else rightLCA
