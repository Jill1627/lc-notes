"""
Permutations有重复
思路：与permutations有三点不同：
1. 遇到i>0 && nums[i] == nums[i - 1]说明当前nums[i]与前一个相同，continue
2. 递归时，将刚刚加入的element移除，递进去的nums是nums[:i] + nums[i + 1:]
3. Base case: nums已无元素剩余
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        if nums is None or len(nums) == 0:
            return res
        nums.sort()
        self.helper(nums, res, [])
        return res
    def helper(self, nums, res, level):
        if len(nums) == 0:
            res.append(list(level))
            return
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            level.append(nums[i])
            self.helper(nums[ : i] + nums[i + 1 : ], res, level)
            level.pop()
