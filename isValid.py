"""
题目：开括号和关括号必须按顺序对应
思路：用stack就可以轻松解决
1. for循环每一个符号，如果是开，就加入stack
2. 如果是关，如果栈空，则没有对应开括号了，就false
   如果不为空，就开最末尾（刚加进去的）符号是否对应的开括号，如果不是，就false
3. 通过这两项false条件后，最终return stack 是否为空，如有剩余，则false
"""

class Solution(object):
    def isValid(self s):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(' or char == ']' and
                    char != '[' or char == '}' and char != '{':
                    return False
                stack.pop()
        return not stack
