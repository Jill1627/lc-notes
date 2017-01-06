"""
问题：给定node p，求它的inorder Successor
思路：用root traverse树
1. 用root寻找p的位置，直到出while循环，出循环后
2. 如果root == None，说明p不存在树种，return root（也就是None）即可
3. root存在，说明停在了p上，那就看p有没有右儿子，如果没有右儿子，successor就是当前s停的地方
4. 若有右儿子，则successor是右儿子的最左左左孙子...
"""

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root or root.val != p.val:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        if not root:
            return root
        if not root.right:
            return successor
        root = root.right
        while root.left:
            root = root.left
        return root
