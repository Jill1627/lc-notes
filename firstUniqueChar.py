# LC 387
""" O(1) space & 1 pass: use find last index of"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1


""" Use hashmap & two pass """
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        hashmap = dict()
        for c in slist:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        for i in range(len(slist)):
            if hashmap[slist[i]] == 1:
                return i
        return -1
