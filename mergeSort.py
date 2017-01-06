"""
问题：sort list
思路：用merge sort，三步: 找中点mid，sort右链，mid.next = None, sort左链，merge左右
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findMid(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        """
        :type head1, head2: ListNode
        :type: ListNode
        """
        if not head1:
            return head2
        if not head2:
            return head1
        dummy = ListNode(0)
        curr = dummy
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)
