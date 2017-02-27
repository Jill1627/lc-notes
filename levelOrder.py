"""
题目：levelOrder输出树值
思路：BFS用Queue
1. 如果root存在，加入queue
2. while queue不为空时：建立level=[]
3. 遍历for此时queue中所有树节，这些树节必定属于同层
4. 逐个树节，先取出当前子节(pop from queue)，将其数值加入levelOrder
5. 若左右子节存在，加入queue，先左后右
6. 出for后，也就是本层以结束，将level加入res
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        queue = deque()
        if root is None:
            return res
        queue.append(root)
        while queue:
            level = []
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(level))
        return res
