"""
LC 494 find target sum ways
Question: given a list of nums, find a set of nums (positive set) and its complimentary set of nums (negative set) such that sum(pve) - sum(nve) = target

Idea: dp
Based on one idea: sum(pve) - sum(nve) = target -> sum(pve) + sum(nve) = sum(all) -> target + sum(all) = 2 * sum(pve)
-> sum(pve) = (sum(all) + target) / 2

Steps:
1. Initialize: calculate total sum of all nums, quick return False if total + target S % 2 is not zero
2. Now the problem becomes: find subset sum equals sum(pve) -> reduce from having to consider +ve and -ve options
3. Helper function: 1d dp: outter loop each num, inner loop from target sum to current num, dp[s] += dp[s - n]
"""

"""Solution 1: smart and tricky"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # initialize
        total = 0
        for n in nums:
            total += n
        # print total
        if total < S or (total + S) % 2 > 0:
            return 0
        return self.subsetSum(nums, (S + total) / 2) # (S + total) / 2 = sum(positive set)

    def subsetSum(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            for s in xrange(target, n - 1, -1):
                dp[s] += dp[s - n]
        return dp[target]
