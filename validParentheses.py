"""
LC 20 Valid parentheses
Idea: stack
Steps:
1. Initialize: use a stack
2. Loop: whenever encounters an open, push a close onto stack; whenever encounters a close, pop one from stack and it should be it!, if stack empty or not the same, return False
3. Exit loop, check whether stack is empty
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False
        # initialize
        stack = list()
        for p in s:
            if p == '(':
                stack.append(')')
            elif p == '[':
                stack.append(']')
            elif p == '{':
                stack.append('}')
            else:
                if len(stack) == 0 or stack.pop() != p: return False
        return len(stack) == 0
