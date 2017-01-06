"""
问题：在一棵二叉树中插入一个新子节
思路：用两种方法解：1）recursion 2）interative
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node
        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

"""
Interative 思路：用两个指针，一前一后，前的一直往下寻找node应该存在的位置；后的跟着前；
后会停在应该insert的位置的parent
"""
class Solution2:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node
        temp = root
        last = None
        while temp:
            last = temp
            if node.val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        if node.val < last.val:
            last.left = node
        else:
            last.right = node
        return root
