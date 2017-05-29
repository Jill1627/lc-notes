"""
LC 150 Evaluation Reverse Polish Notation
Use stack
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None or len(tokens) == 0:
            return 0
        stack = list()
        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 / num2)
            else:
                stack.append(int(tok))
        return stack.pop()
