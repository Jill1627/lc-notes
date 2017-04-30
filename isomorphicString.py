class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hm = dict()
        seen = set()
        for i in xrange(len(s)):
            if s[i] not in hm:
                hm[s[i]] = t[i]
                if t[i] in seen:
                    return False
                seen.add(t[i])
            else:
                if hm[s[i]] != t[i]:
                    return False
        return True
