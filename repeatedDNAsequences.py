"""
LC.187 Repeated DNA sequences
use hashmap or set
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0:
            return []
        res = list()
        hm = dict()
        for i in xrange(len(s) - 9):
            substr = s[i : i + 10]
            if substr in hm:
                if substr not in res:
                    res.append(substr)
            else:
                hm[substr] = 1
        return res
