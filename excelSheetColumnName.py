"""
LC 168 Excel Sheet Column Name
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ordA = ord('A')
        res = ""
        while n > 0:
            n -= 1
            c = chr(ordA + (n % 26))
            res = c + res
            n /= 26
        return res
