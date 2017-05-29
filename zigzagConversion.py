"""
LC.6 Zigzag conversion
Very easy if draw out index graph

given a string with length of 10, index 0 - 9
numRows = 3, graph below:

0  4   8
1 3 5 7 9
2    6   10

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        res = list()
        n = numRows
        for i in xrange(n):
            res.append(list())
        i = 0
        while i < len(s):
            for index in range(n):
                if i >= len(s): break
                res[index].append(s[i])
                i += 1
            for index in range(n - 2, 0, -1):
                if i >= len(s): break;
                res[index].append(s[i])
                i += 1
        for i in xrange(len(res)):
            res[i] = "".join(res[i])
        return "".join(res)
