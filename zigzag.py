"""
思路：用两个stacks，相互捯饬
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        if not root:
            return res
        stack = [root]
        nextStack = list()
        levelIndex = 0
        while stack:
            level = list()
            while stack:
                node = stack.pop()
                level.append(node.val)
                if levelIndex % 2 == 0:
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
                else:
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            res.append(level)
            tmp = stack
            stack = nextStack
            nextStack = tmp
            levelIndex += 1
        return res
