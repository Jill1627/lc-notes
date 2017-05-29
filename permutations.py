"""
LC 46 Permutations
思路: backtracking
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return nums

        res = list()
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, level):
        if len(level) == len(nums):
            res.append(list(level))
            return
        for i in nums:
            if i not in level:
                level.append(i)
                self.helper(nums, res, level)
                level.pop()
