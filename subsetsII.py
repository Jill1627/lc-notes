"""
1. sort
2. Remove duplicate
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        if not nums or len(nums) == 0:
            return result
        nums.sort()
        self.recur_helper(result, [], nums, 0)
        return result
    def recur_helper(self, result, path, nums, startIndex):
        # if startIndex > len(nums):
        #     return
        result.append(list(path))
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.recur_helper(result, path, nums, i + 1)
            path.pop()
