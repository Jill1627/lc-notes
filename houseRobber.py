"""LC 198 House Robber"""

""" O(n) time O(n) space dp My own solution"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        total = [nums[i] for i in xrange(len(nums))]
        # for i in xrange(len(nums)):
        #     total[i] = nums[i]
        total[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            total[i] = max(total[i - 1], total[i - 2] + nums[i])
        return total[len(nums) - 1]

""" O(n) time O(1) space My own solution """
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prevprev = nums[0]
        prev = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            curr = max(prevprev + nums[i], prev)
            prevprev = prev
            prev = curr
        return curr

""" O(n) time O(1) space """
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, prevPrev = 0, 0
        for i in nums:
            prevPrev, prev = prev, max(prevPrev + i, prev)
        return prev
