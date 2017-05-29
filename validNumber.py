"""
LC. 65 Valid number
Strategy: a bunch of ifs
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        number = False
        e = False
        point = False
        numberAfterE = True
        for i in xrange(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                number = True
                numberAfterE = True
            elif s[i] == '.':
                if (point or e):
                    return False
                point = True
            elif s[i] == 'e':
                if (e or not number):
                    return False
                numberAfterE = False
                e = True
            elif s[i] == '+' or s[i] == '-':
                if (i != 0 and s[i - 1] != 'e'):
                    return False
            else:
                return False
        return number and numberAfterE
