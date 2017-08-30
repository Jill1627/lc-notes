"""
LC 44 Wildcard Matching

Idea:
2d dp

Steps:
1. initialize: 2d array with outter as pattern, inner as source, dp[0][0] = True
2. loop: within p, whenever sees a '*', dp[i][0] = True if dp[i - 1][0] is True
3. inner loop of s, 2 conditions: 1) p at i is not a '*' 2) is a '*'
4. not a '*', just compare current char equal or ?, based on prev
5. is a '*', star can either represents zero char or one - multiple char
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # legal check
        if len(p) - p.count('*') > len(s):
            return False
        # initialize
        dp = [[False] * (len(s) + 1) for i in xrange(len(p) + 1)]
        dp[0][0] = True
        # loop
        for i in xrange(1, len(p) + 1):
            if p[i - 1] == '*' and dp[i - 1][0]:
                dp[i][0] = True
            for j in xrange(1, len(s) + 1):
                if p[i - 1] != '*':
                    if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[len(p)][len(s)]
