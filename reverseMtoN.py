# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m >= n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for i in range (1, m):
            head = head.next
        preM = head
        mNode = head.next
        nNode = mNode
        postN = nNode.next
        for i in range (n - m):
            if not postN:
                return dummy.next
            temp = postN.next
            postN.next = nNode
            nNode = postN
            postN = temp
        preM.next = nNode
        mNode.next = postN
        return dummy.next
            
