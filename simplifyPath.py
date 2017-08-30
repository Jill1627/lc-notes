"""
LC 71 simplify path
Idea:
use stack, set

Steps:
1. initialize, a stack, a set of skipping characters "..", ".", ""
2. Loop through each element splitted by '/', pop from stack if it's ".." and stack is not empty; otherwise, add to stack if it's not skipping characters
3. loop through stack to construct the result, connect with '/'
4. If nothing left in stack and res would be empty, simply return "/"
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path is None or len(path) == 0:
            return path
        # initialize
        res = ""
        stack = list()
        skip = {"..", ".", ""} # a set
        # loop to construct stack
        for directory in path.split("/"):
            if directory == ".." and len(stack) != 0:
                stack.pop()
            elif directory not in skip:
                stack.append(directory)
        # loop stack to construct result
        for directory in reversed(stack):
            res = "/" + directory + res
        return res if len(res) > 0 else "/"
