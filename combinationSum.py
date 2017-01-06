"""
问题：找出所有combination使得目标sum等于target
思路：backtracking (use recur_helper)
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        if candidates is None or len(candidates) == 0:
            return result
        self.recur_helper(result, path, 0, target, candidates)
        return result

    def recur_helper(self, res, path, start, target, candidates):
        if target < 0:
            return
        if target == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.recur_helper(res, path, i, target - candidates[i], candidates)
            path.pop()
