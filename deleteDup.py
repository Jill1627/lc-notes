"""
问题：在排序的LL中去除重复的节点，重复的节点一个copy都不留 1-2-2-3-4 -> 1-3-4
思路：用一个dummy node，一直比较指针curr的next和next.next
1. dummy在head前，curr指向dummy
2. while循环遍历LL，条件是next和next.next都存在
3. 每次比较next和nextnext的值，一旦相同，将value存下，进入内while循环；不相同就下一个
4. 内while的条件是，curr.next存在，且val==value，如此就去除
完成
"""

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                value = curr.next.val
                while curr.next and curr.next.val == value:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
