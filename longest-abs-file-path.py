"""
String handling
A few python built-ins:
1. str.splitlines()
2. str.lstrip('char')
3. len(str) - where \ is not counted
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if input is None or len(input) == 0:
            return 0
        maxLen = 0
        pathLen = {0 : 0}
        for line in input.splitlines():
            name = line.lstrip("\t") # remove \t
            depth = len(line) - len(name) # depth = # of 't' in front
            if '.' in name:
                maxLen = max(maxLen, pathLen[depth] + len(name)) # last depth's len + curr len
            else:
                pathLen[depth + 1] = pathLen[depth] + len(name) + 1 # add this depth's len into hashmap, + 1 means include '/'
        return maxLen
