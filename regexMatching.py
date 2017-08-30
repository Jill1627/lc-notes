"""
LC 10 Regular expression matching
Idea: 2d dp divide into 2 major conditions

Steps:
1. Initialize dp[n + 1][m + 1] booleans - extra consider the condition dp[0] row, whenever p[i] is a '*', dp[0][i] = dp[0][i - 2], as that * cancels its precedence

2. Loop thru s and loop thru p, consider 2 major conditions:
case 1: when s[i] == p[j] or p[j] == '.'
case 2: when p[j] == '*', 2 sub conditions

3. Within case 2 above, p[j] == '*', consider 2 sub conditions:
case 1: when char before * does not match in any of the 2 following ways
case 2: when char before * in p matches char in s, either '.' or alpha

"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for i in xrange(m + 1)]

        # initialize
        dp[0][0] = True
        # dp first row empty s, so if any spot p char == *, it matches zero char in s
        for i in xrange(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        # fill 2d array dp
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                # s char matches p char as alphabetical, or p char is '.'
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # p char is '*'
                elif p[j - 1] == '*':
                    # p char before '*' does not match s char alpha, or is not '.' --> '*' represents 0 * p[i - 2] - remove p[i - 2]
                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    # p char before * matches
                    else:
                        dp[i][j] = dp[i][j - 1] # * matches 1
                        or dp[i][j - 2] # * matches 0
                        or dp[i - 1][j] # * matches multiple
        return dp[m][n]
