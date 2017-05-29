"""
LC. 297 Serialize and Deserialize Binary Tree
Strategy: from tree to string, and from string to tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    splitter = ","
    nullmark = "x"

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        treeList = list()
        self.buildString(root, treeList)
        return ''.join(treeList)

    def buildString(self, node, treeList):
        if node is None:
            treeList.append(self.nullmark)
            treeList.append(self.splitter)
        else:
            treeList.append(str(node.val))
            treeList.append(self.splitter)
            self.buildString(node.left, treeList)
            self.buildString(node.right, treeList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        nodes = deque(data.split(self.splitter))
        return self.buildTree(nodes)

    def buildTree(self, nodes):
        val = nodes.popleft()
        if val == self.nullmark:
            return None
        else:
            node = TreeNode(val)
            node.left = self.buildTree(nodes)
            node.right = self.buildTree(nodes)
            return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
