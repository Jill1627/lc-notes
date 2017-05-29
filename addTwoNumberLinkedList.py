""" 2. Add Two Numbers """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        total = 0
        while l1 or l2:
            total /= 10
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            head.next = ListNode(total % 10)
            head = head.next
        if total / 10 == 1:
            head.next = ListNode(1)
        return dummy.next
