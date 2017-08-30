"""
问题：一个list中有K个LL，全部merge成一条升序的LL
思路：merge 2 by 2
1. while lists中还有超过一个LL时，说明merge尚未完成，继续merge
2. for每两个LL，merge。注意！别忘了单数个LL的情况，最后一个还要加入下一轮merge
3. helper method merge
4. 每一轮merge完，将lists = newList 再合并一轮，直到所有都成一条LL
完成

*********有空看一下priority queue解法*************** Get!
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        while len(lists) > 1: # in list of LL, when there are more than 1 LL
            size = len(lists)
            newList = list()
            for i in range(0, size - 1, 2): # inner loop for all LLs to merge
                mergedList = self.merge(lists[i], lists[i + 1])
                newList.append(mergedList)
            if size % 2 == 1:
                newList.append(lists[size - 1])
            lists = newList
        return lists[0]
    def merge(self, head1, head2):
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
