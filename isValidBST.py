# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
问题：检查一棵树是否二叉树
思路：stack，两个pointer：curr 和 prev
1. curr存在，就加入stack，并往左走
2. curr不存在，就pop stack，比较值，更新prev到node，curr到node.right
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = list()
        curr = root
        prev = None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if prev and node.val <= prev.val:
                    return False
                prev = node
                curr = node.right
        return True
