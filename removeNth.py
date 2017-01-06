"""
问题：remove倒数第n个节点
思路：用一个dummy node，用两个Pointers
1. 建一个dummy，pointer curr，在head前面
2. 先让head到n的位置
3. 让head和curr同时往后，head到底，curr正好停在倒数n的前面
4. curr.next = curr.next.next
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNth(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        assume: n is valid
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        "Move head to nth node"
        for i in range(n):
            "Check if n > list's length"
            if not head:
                return dummy.next
            head = head.next
        while head: #head is not None
            head = head.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
