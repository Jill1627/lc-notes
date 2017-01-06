"""
问题：问总共有多少条路径，从任意节点往下走，等于given sum。不必从根到root，必须从上至下
思路：DFS
1. 主程序 = 数以当前节点为起点的符合条件路径数 + recur左 + recur右
2. 辅助程序，及数以当前节点为起点的符合条件路径数，不断update res
3. res+1的条件包括，当前根等于sum
4. res+= 以左子节为起点的符合路径数 & 右
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.counter(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def counter(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res = 0
        if not root:
            return res
        if root.val == sum:
            res += 1
        res += self.counter(root.left, sum - root.val)
        res += self.counter(root.right, sum - root.val)
        return res
