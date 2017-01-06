"""
问题：找从根到叶的最大和
思路：recur左子树，右子树，>0就+root；<0就是0+root
"""

class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        if not root:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        return max(0, max(left, right)) + root.val
