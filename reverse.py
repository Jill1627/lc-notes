"""
问题：反转LL
prev = None作为新尾巴
loop中，重连
"""

""" My own solution iterative """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # iteratively
        tail = None
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
        curr.next = tail
        return curr

""" Recursively """
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        headnext = head.next
        newHead = self.reverseList(head.next)
        headnext.next = head
        head.next = None
        return newHead

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
