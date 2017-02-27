# LC225
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if not self.q1:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
