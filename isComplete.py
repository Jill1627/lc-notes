"""
问题: 问一棵树是否完全
思路：使用队列 Queue装入所有TreeNode，pop掉所有尾端的None，然后逐个检查，一旦中间有None，false
1. 将root装进queue
2. 用指针index，记录queue中的元素
3. 当index未达到队列长度时，意味着队列中还有实际的元素，就先测试该元素的左右儿子是否存在，然后加入队列
4. 加入完毕后，将靠后的None元素全部pop掉，会停止在一个实际元素的位置
5. for所有当前队列中的元素，任何是否出现空，都false，其他true。因为现在出现的None元素，就是树中间的，而不是尾后的
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        if not root:
            return True
        q = [root]
        index = 0
        while index < len(q):
            if q[index]:
                q.append(q[index].left)
                q.append(q[index].right)
            index += 1
        while not q[-1]:
            q.pop()
        for node in q:
            if not node:
                return False
        return True
