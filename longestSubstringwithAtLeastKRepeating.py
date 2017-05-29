"""
LC 395 Longest substring with at least k repeating characters

Use recursion, if there is char with < k occurrence, split it by this char
and recur on both ends substring
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
