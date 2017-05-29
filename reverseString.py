"""
LC. 344 Reverse String
Recursive
Iterative
"""

""" Own solution: recursion - might exceeds memory limit """
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0 or len(s) == 1:
            return s
        return s[-1] + self.reverseString(s[:-1])

""" Own solution: iterative - Two pointers """
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0 or len(s) == 1:
            return s
        i = 0
        j = len(s) - 1
        listS = list(s)
        while i < len(s) / 2:
            listS[i], listS[j] = listS[j], listS[i]
            i += 1
            j -= 1
        return "".join(listS)
