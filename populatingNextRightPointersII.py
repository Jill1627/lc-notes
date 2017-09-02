"""
LC 117 Populating next right pointers in each nodes II
difference than 116, here it's not a perfect (full) binary tree

Ideas: level order traversal of binary tree
Double while loop

Steps:
1. Outter while loop for each level: create a new dummy node before the head of this level
2. Inner loop for each node within a level lower than root: if root's left exists, connect curr.next = root.left, and move curr to next; do the same for right child - move root to the next
3. exiting inner loop, move root to dummy.next - head of the level 
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
        if root is None: return root
        # outter loop for each level
        while root:
            dummy = TreeLinkNode(0) # create a dummy node
            curr = dummy # curr pointer starts from dummy node
            # inner loop for each node on the same level
            while root:
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                root = root.next
            root = dummy.next
