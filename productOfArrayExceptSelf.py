"""
LC 238. Product of array except self
Idea: similar to prefix sum, use prefix product
2 pass for loop, second loop in reverse order

Steps:
1. generate an array of prefix product except self: res
2. loop through res in reverse order, *= postfix in each iteration, maintain a variable postfix, cumulative product in reverse order
"""

""" O(n) time O(1) space """
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        if not nums or len(nums) == 0:
            return res
        # initialize res, first element = 1, add all prefix product except self
        res.append(1)
        for i in xrange(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])
        # update res with second half
        postfix = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



""" my own solution O(n) time O(n) space """
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        if nums is None or len(nums) == 0:
            return res
        n = len(nums)
        # create prefix product array
        prefix = [nums[0]]
        for i in xrange(1, n):
            prefix.append(nums[i] * prefix[i - 1])
        # create postfix product array
        postfix = [nums[i] for i in xrange(len(nums))]
        for i in xrange(n - 2, 0, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        # create res array
        res = [0 for i in xrange(len(nums))]
        for i in xrange(n):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i < n - 1:
                res[i] = prefix[i - 1] * postfix[i + 1]
            else:
                res[i] = prefix[i - 1]
        return res
