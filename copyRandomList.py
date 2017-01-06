"""
问题：深度复制一个带有random pointer的LL，就是每个node有两个pointer, next, random
思路：先遍历复制与原LL中，将新节点的random pointer连好，拆分
1. 将list 1-2-3 --> 1-1'-2-2'-3-3'
2. fix random pointer
3. 拆分出新LL
4. 格外注意None checks
完成
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        self.makeCopy(head)
        self.copyRandom(head)
        return self.split(head)
        
    def makeCopy(self, head):
        """
        :type head: RandomListNode
        :rtype: void
        """
        while head:
            copy = RandomListNode(head.label)
            copy.next = head.next
            copy.random = head.random
            head.next = copy
            head = head.next.next
    def copyRandom(self, head):
        """
        :type head: RandomListNode
        :rtype: void
        """
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next
    def split(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        newHead = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            if tmp.next:
                tmp.next = tmp.next.next
        return newHead
