"""
问题：输入tree和int sum，问有没有一条路径和等于sum，输出如有
思路：backtracking
1. 主程序使用res和path
2. helper method updates res and pathSum
3. 如果root不存在了，return
4. 将当前root.val 加入path
5. 如果只剩下root一个node，且val == sum，就把当前path加入res；删除path的最后一个元素
6. 如果还有更多nodes，recur
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
        :rtype: List[List[int]]
        """
        res = list()
        path = list()
        self.findPath(root, sum, res, path)
        return res
    def findPath(self, root, sum, res, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and sum == root.val:
            res.append(list(path))
            path.pop()
            return
        else:
            self.findPath(root.left, sum - root.val, res, path)
            self.findPath(root.right, sum - root.val, res, path)
        path.pop()
