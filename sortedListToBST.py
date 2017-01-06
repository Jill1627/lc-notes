"""
# 重点基础题
问题：将升序的LL建立成balanced BST
思路：DFS recursion, Inorder traversal
1. 数出LL的长度 size
2. helper method treeBuilder：检查条件: start > end, return None
3. 建立顺序：左子树，根，（LL node后移），左根连接，右子树，右根连接
4. return root
完成
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        size = 0
        self.node = head
        while head:
            head = head.next
            size += 1
        return self.treeBuilder(0, size - 1)
    def treeBuilder(self, start, end):
        if start > end:
            return None
        mid = start + (end - start) / 2
        left = self.treeBuilder(start, mid - 1)
        root = TreeNode(self.node.val)
        root.left = left
        self.node = self.node.next
        right = self.treeBuilder(mid + 1, end)
        root.right = right
        return root
