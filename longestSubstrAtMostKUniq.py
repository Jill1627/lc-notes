"""
LC 340 Longest substring with at most K distinct characters
two pointers sliding window
"""

""" Use hashmap to keep track of char and its occurence """
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        j = 0
        longest = 0
        hm = dict()

        for i in xrange(len(s)):
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1
            while len(hm) > k:
                hm[s[j]] -= 1
                if hm[s[j]] == 0:
                    hm.pop(s[j])
                j += 1
            longest = max(longest, i - j + 1)
        return longest



""" Use hashmap to keep track of index of each char """
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        j = 0
        longest = 0
        hm = dict()
        for i in xrange(len(s)):
            hm[s[i]] = i
            if len(hm) > k:
                while hm[s[j]] != j:
                    j += 1
                hm.pop(s[j])
                j += 1
            longest = max(longest, i - j + 1)
        return longest
