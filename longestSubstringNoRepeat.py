#LC3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0
        longest = 0
        seen = dict() # map char with its index
        j = 0 # left pointer
        for i in range(len(s)):
            if s[i] in seen:
                j = max(j, seen[s[i]] + 1)
            seen[s[i]] = i
            longest = max(longest, i - j + 1)
        return longest
