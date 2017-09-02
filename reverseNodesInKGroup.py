"""
LC 25 Reverse nodes in K Group - given a constant k, reverse k nodes as a group within a linked list

Idea: recursive or iterative
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" Recursive solution - see in line comment """
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # initialize
        count = 0 # number of nodes
        curr = head

        # base case - only look at part of linked list within k nodes
        while curr and count < k: # exit if reaching the end OR count == k, curr stops at k + 1th node
            curr = curr.next
            count += 1

        # check: if less than k nodes
        if count < k: return head

        # recursion - get next group of reversed nodes
        curr = self.reverseKGroup(curr, k) # curr now is the head of next piece of reversed k - param curr is at k + 1 node

        # loop - reverse
        while count > 0:
            temp = head.next
            head.next = curr
            curr = head
            head = temp # head stops at next group's head
            count -= 1 # count last value = 0, all nodes are reversed 

        head = curr
        return head
