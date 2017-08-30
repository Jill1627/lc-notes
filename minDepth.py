"""
问题：求一棵树的最小高度（深度）
思路：recur，分四种情况
1. 该子节无左右儿子（到底了）：return 0
2. 该字节无左儿子，有右儿子：return 右儿子minDepth + 1
3. 该子节无右儿子，有左儿子：同上 反之
4. 该子节有左右儿子：选取左右儿子的minDepth中的偏小值，+ 1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

"""
Solution 2 - better
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1
