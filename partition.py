"""
问题：给一条LL，和一个数x，把小于x的都放左边，大于x的放右边，原相对顺序不变
思路：用两个dummy,left and right，分别连接
1. 遍历整个LL，比x小的，接在left后，left更新为当前head；比x大的，同理right
2. 重连left和right
"""

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)
        left, right = leftDummy, rightDummy
        # 遍历整个LL
        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next
        # 重连left，right
        right.next = None
        left.next = rightDummy.next
        return leftDummy.next
