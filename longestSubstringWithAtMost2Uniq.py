"""
LC 159 Longest substring with at most 2 distinct characters
Two pointers sliding window
"""

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        longest = 0
        j = 0
        hm = dict()
        for i in xrange(len(s)):
            hm[s[i]] = i
            if len(hm) > 2:
                while s[j] not in hm or hm[s[j]] != j:
                    j += 1
                # print hm
                hm.pop(s[j], None)
                j+=1
            longest = max(longest, i - j + 1)
        return longest
