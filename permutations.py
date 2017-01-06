"""
思路: backtracking
"""

class Solution(object):
    def permutations(self, nums):
        result = list()
        if nums is None or len(nums) == 0:
            return result
        self.recur_helper(result, [], nums)
        return result
    def recur_helper(self, res, path, nums):
        if len(path) == len(nums):
            res.append(list(path))
        for i in nums:
            # 与combination的区别在此：因为每个数每次都要，所以不需要起始位置，只需要测试
            # 此轮是否已经加入
            if i not in path:
                path.append(i)
                self.recur_helper(res, path, nums)
                path.pop()
