#LC14
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ""
        pre = strs[0]
        for i in range(len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[: len(pre) - 1]
        return pre

"""My own AC solution"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        n = len(strs[0])
        res = ""
        for i in range(n):
            c = strs[0][i]
            for word in strs:
                if i > len(word) - 1 or word[i] != c: return res
            res = res + c
        return res
