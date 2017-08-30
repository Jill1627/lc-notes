# LC139 Word Break Google, Facebook, Uber, Amazon, Yahoo, Bloomberg
""" DP: f(i) up to char at index i, excluding i, whether it can be breaked into words in dictionary

Steps:
1. Set up 1d boolean array with size of len(s) + 1
2. function dp[i] is defined as whether substring s[: i] is breakable
3. subproblem dp[i] can be repeatedly updated as j going through each pos within the range of i
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
            """ Potential Improvement: check maxLen of w in wordDict """
            # for j in range(min(i, j + maxLen + 1)):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
