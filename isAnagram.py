class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        count = dict()
        for c in s:
            count[c] = count[c] +1 if c in count else 1
        for c in t:
            count[c] = count[c] - 1 if c in count else -1
        for i in count:
            if count[i] != 0:
                return False
        return True
