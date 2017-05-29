"""
问题：实现一个minStack,以及push(), pop(), top(), 和getMin()
思路：用两个stacks 一个regular，一个min,也就是python中的list啦
1. push（）的时候先把number直接加上regular，只有在min是空的时候或者新数字比min top小的时候加入min stacks
2. pop()，先把regular stack的pop出来，如果regular和min的top值相等，就把min也pop了
3. top（）就是看regular的最上一位
4. getMin()就是看min的最上一位
"""

""" My own solution with two stacks """
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.reg = list()
        self.minstack = list()


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.reg.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        popped = self.reg.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.reg:
            return self.reg[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

""" solution """

class MinStack:

def __init__(self):
    self.q = []

# @param x, an integer
# @return an integer
def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
        curMin = x
    self.q.append((x, curMin));

# @return nothing
def pop(self):
    self.q.pop()


# @return an integer
def top(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][0]


# @return an integer
def getMin(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][1]
