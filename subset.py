"""
Use backtracking
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        if nums is None or len(nums) == 0:
            return result
        self.recur_helper(result, path, nums, 0)
        return result
    def recur_helper(self, res, path, nums, index):
        res.append(list(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.recur_helper(res, path, nums, i + 1)
            path.pop()
