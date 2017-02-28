""" LC116 """

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
        if root is None: return
        pre = root # pre will always be left most node of each level
        while pre.left:
            curr = pre
            while curr: # when exit, done with this level, curr == None
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next # curr moves one node to the right
            pre = pre.left # advance to a lower level
