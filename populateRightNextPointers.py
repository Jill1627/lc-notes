"""
LC.116 Populating Next Right Pointers in Each node
Strategy: use two pointers: pre and curr
pre - iterate all leftmost nodes of each level
curr - iterate all nodes on a level
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        pre = root
        # pre iterate leftmost node of each level
        while pre.left:
            curr = pre
            # curr iterate every node on a level
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            pre = pre.left
