"""
LC 341 Flatten nested list Iterator
1. initialize in constructor: use a stack, and push all items in reverse order
2. next: pops the top of stack's integer value
3. hasNext: while stack not empty, get ready the top item's elements
- Peek the top element on the stack: if it is a Integer element: return True
- If it's a list, pop the list, and push all elements within it onto stack in reverse order, until the top element is an Integer element
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = list()
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            # if top of stack is already an integer, immediately return True
            top = self.stack[-1]
            if top.isInteger(): return True
            # otherwise, pop the list and push all elements onto stack backwards
            self.stack.pop()
            for item in reversed(top.getList()):
                self.stack.append(item)
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
