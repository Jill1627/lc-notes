"""
LC 3. Longest substring with No repeating characters
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        i = j = 0
        hm = dict()
        longest = 0
        for i in xrange(len(s)):
            if s[i] in hm:
                j = max(j, hm[s[i]] + 1)
            hm[s[i]] = i
            longest = max(longest, i - j + 1)
        return longest
