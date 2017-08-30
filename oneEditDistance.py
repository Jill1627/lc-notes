"""
LC 161 Given two strings, see if they are one edit distance from each other
1. loop through the shorter one
2. when encounter a different char
3. three situations: 1) length equal 2) s longer than t 3) s shorter than t
4. If all chars are equal, check if the length difference is 1
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None: return False

        for i in xrange(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1 : ] == t[i + 1 : ]
                if len(s) > len(t):
                    return s[i + 1 : ] == t[i : ]
                else:
                    return s[i : ] == t[i + 1 : ]
        return abs(len(s) - len(t)) == 1
