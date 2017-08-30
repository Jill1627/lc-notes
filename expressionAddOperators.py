"""
LC 282 Expression Add Operators [hard]
Key: backtracking
use recursion helper method for each level of recursion
loop through each possible substring number

Steps:
1. Enters recursion with res, path, num, target, starting pos, tempRes and carry
2. Recursion base case: when tempRes equals to target, and, starting pos reaches the end of num string
3. If at any time, substring starts with a zero and have more following, break
4. If starting pos is zero, path edits differently
5. In non zero starting pos, try out add, subtract, multiplication options
6. Make notice of multed variable

trick: last parameter multed - specially for multiplication
multed = the change last (current level's previous) level made on top of its previous level (current level's previous previous)
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = list()

        if not num or len(num) == 0:
            return res

        self.helper(res, "", num, target, 0, 0, 0)
        return res

    # recursion helper for backtracking
    def helper(self, res, path, num, target, pos, tempRes, multed):

        if tempRes == target and len(num) == pos:
            res.append(path)
            return

        for i in xrange(pos, len(num)):
            # if encounter any substring starts from 0, break
            if i != pos and num[pos] == '0': break

            currStr = num[pos : i + 1]
            currNum = int(currStr)

            if pos == 0: # right now, path is empty string
                self.helper(res, path + currStr, num, target, i + 1, currNum, currNum)
            else:
                self.helper(res, path + "+" + currStr, num, target, i + 1, tempRes + currNum, currNum)
                self.helper(res, path + "-" + currStr, num, target, i + 1, tempRes - currNum, -currNum)
                self.helper(res, path + "*" + currStr, num, target, i + 1, tempRes - multed + multed * currNum, multed * currNum)
