"""
Python built-ins:
1. str.upper()
2. str.replace('-', '')
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '') # make string into all upper cases without -
        size = len(S)
        index = K if size % K == 0 else size % K # handle group 1
        result = S[:index] # handle remaining string
        while index < size:
            result += '-' + S[index : index + K]
            index += K
        return result
