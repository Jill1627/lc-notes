"""
LC 404 Sum of left leaves of binary tree

Idea: recursive or iterative

Recursive solution steps:
1. base case 1) when root is None, return 0; 2) if root.left exists, check whether it's a leaf, if so, add it to res
2. if not, recur
3. recur on right child

Iterative solution steps:
1. use a stack, only push onto stack when left child is not a leaf, and when right child is not a leaf; if left child is a leaf, update result; do nothing when right child is a leaf
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
""" Recursive solution """
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        # base case
        if root.left: # check whether this left child is leaf
            if root.left.left is None and root.left.right is None:
                res += root.left.val
            # recurrence
            else:
                res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res

""" Iterative solution """
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        # initialize
        stack = list()
        stack.append(root)
        res = 0
        # loop
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    res += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if node.right.left is not None or node.right.right is not None: # only push onto stack when this right is not a leaf, it's worth going down further
                    stack.append(node.right)
        return res
