"""
LC 23 Merge K sorted list
Use PQ
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if lists is None or len(lists) == 0:
            return lists

        q = PriorityQueue()
        dummy = ListNode(0)
        curr = dummy

        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            currMin = q.get()[1]
            curr.next = currMin
            curr = curr.next
            if currMin.next:
                q.put((currMin.next.val, currMin.next))
        return dummy.next
