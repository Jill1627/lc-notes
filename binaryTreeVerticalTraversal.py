"""
314 Binary tree vertical traversal
Idea: 2 queues + hashmap + BFS

Steps:
1. A queue for node
2. A queue for col number - horizontal distance from node to root (left: -ve)
3. A hashmap [colNumber : list of Nodes on this colNum]
4. minimum and maximum to keep track of min and max col no. to easily traverse hm for result
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        if root is None:
            return res

        nodeQ = deque()
        colQ = deque()
        hm = dict()
        minimum = 0
        maximum = 0

        nodeQ.append(root)
        colQ.append(0)

        while nodeQ:
            node = nodeQ.popleft()
            col = colQ.popleft()
            # update the hashmap
            if col not in hm:
                hm[col] = list()
            hm[col].append(node.val)
            # go to left child
            if node.left:
                nodeQ.append(node.left)
                colQ.append(col - 1)
                minimum = min(minimum, col - 1)
            # go to right child
            if node.right:
                nodeQ.append(node.right)
                colQ.append(col + 1)
                maximum = max(maximum, col + 1)
        # loop through hashmap from min to max
        for i in xrange(minimum, maximum + 1):
            res.append(hm[i])

        return res
