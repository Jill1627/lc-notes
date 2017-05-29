""" LC 76 Minimum Window Substring """


import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        j = 0
        start = -1
        hmS = dict()
        hmT = dict()
        count = 0
        minSize = sys.maxint

        for i in xrange(len(t)):
            if t[i] in hmT:
                hmT[t[i]] += 1
            else:
                hmT[t[i]] = 1

        for i in xrange(len(s)):
            if s[i] in hmS:
                hmS[s[i]] += 1
            else:
                hmS[s[i]] = 1
            if s[i] in hmT and hmS[s[i]] <= hmT[s[i]]:
                count += 1
            if count == len(t):
                while s[j] not in hmT or hmS[s[j]] > hmT[s[j]]:
                    if s[j] in hmT:
                        hmS[s[j]] -= 1
                    j += 1
                windowSize = i - j + 1
                if windowSize < minSize:
                    start = j
                    minSize = windowSize
        if start > -1:
            return s[start : start + minSize]
        return ""
