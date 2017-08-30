'''
LC 125 iterative solution
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return True
        # remove space and special characters, and conver to lower cases
        alphaS = "".join(c for c in s if c.isalnum()).lower()

        for i in xrange(len(alphaS) / 2):
            if alphaS[i] != alphaS[len(alphaS) - 1 - i]:
                return False
        return True
