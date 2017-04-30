# LC152 Maximum Product Subarray
""" Keep track of currMax and currMin """

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        premax, premin, allmax, allmin = nums[0], nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            imax = max(nums[i], nums[i] * premax, nums[i] * premin)
            imin = min(nums[i], nums[i] * premax, nums[i] * premin)
            allmax = max(imax, allmax)
            premax = imax
            premin = imin
        return allmax
