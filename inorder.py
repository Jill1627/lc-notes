"""
思路：iterative 用stack，先把左的左全部加入，然后一个一个pop出来，加入右
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        if not root:
            return res
        stack = list()
        curr = root
        while curr or stack:
            while curr: # only add existing node to the stack
                stack.append(curr)
                curr = curr.left # go for its left child
            curr = stack.pop() # the popped node is the lowest left at the moment, ready to be added into result
            res.append(curr.val)
            curr = curr.right
        return res
