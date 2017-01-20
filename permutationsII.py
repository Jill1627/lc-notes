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
        result = list()
        if nums is None or len(nums) == 0:
            return result
        nums.sort()
        self.recur_helper(result, [], nums)
        return result
    def recur_helper(self, result, path, nums):
        if len(nums) == 0:
            result.append(list(path))
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.recur_helper(result, path, nums[:i] + nums[i + 1:])
            path.pop()
