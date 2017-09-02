"""
LC 234 Palindrome Linked List

2 solutions: 1. O(n) space with a stack; 2. O(1) space with reversing half

Solution 1:
Steps:
1. initialize: stack append head val, fast and slow pointer to find middle
2. compare each val with stack.pop()

Solution 2:
Steps:

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" O(n)  with a stack """
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # legal check
        if head is None or head.next is None:
            return True
        # initialize
        stack = list()
        fast = head
        slow = head
        stack.append(head.val)
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            stack.append(slow.val)
        # when number of ListNode is odd, pop the middle one (top of stack)
        if fast.next is None:
            stack.pop()
        while slow.next:
            slow = slow.next
            if slow.val != stack.pop(): return False
        return True

""" O(1) space, reverse second half of linked list """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # empty list or list of 1 single node is Palindromic
        if head is None or head.next is None:
            return True
        # find middle node of linked list:
        # slow stops at middle if total is odd, at middle - 1 if even
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half of linked list
        prev = None
        secondHalf = slow.next
        while secondHalf.next:
            tmp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tmp
        # compare first half and second half
        firstHalf = head
        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            secondHalf = secondHalf.next
            firstHalf = firstHalf.next
        return True
