# 409 Longest Palindrome
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        count = 0
        hs = set()
        for i in range (len(s)):
            if s[i] in hs:
                hs.remove(s[i])
                count += 1
            else:
                hs.add(s[i])
        if len(hs) != 0:
            return count * 2 + 1
        else:
            return count * 2
