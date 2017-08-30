"""
LC 377 Combination Sum 4
Idea: bottom up dp
Steps:
1. initialize dp with size of target + 1
2. dp function = how many ways to form this target Sum
3. loop through each target sum, inner loop through each element in the nums list, if target sum - num >= 0, meaning it can be formed
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 1 if target == 0 else 0
        # initialize
        dp = [0] * (target + 1)
        dp[0] = 1
        # function - how many ways to form this target sum
        for i in xrange(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
