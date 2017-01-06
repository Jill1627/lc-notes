"""
问题：给一棵树和一个sum，求问有没有一条根到叶的路径和==sum
思路：recursion
1. 如果root不存在，false
2. 如果树只有一个root节点，且root.val == sum，true
3. sum更新 -= root.val
4. return 左右子树有任何一个的结果 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return left or right
