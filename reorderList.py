"""
问题：将LL 1-2-3-4-5-6 --> 1-6-2-5-3-4
思路：分三步 1）找到中点，并把mid.next = None 2) 将后半部reverse 3)merge
注意merge按照index % 2 进行
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.findMiddle(head)
        tail = self.reverse(mid.next)
        mid.next = None
        self.merge(head, tail)
    def findMiddle(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self, head):
        if not head or not head.next:
            return head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    def merge(self, head1, head2):
        if not head1 or not head2:
            return
        dummy = ListNode(0)
        index = 1
        while head1 and head2:
            if index % 2 == 1:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
