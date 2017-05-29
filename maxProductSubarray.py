"""
LC152 Maximum Product Subarray
Keep track of currMax and currMin, prevMax, prevMin, and overall max as result 
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        # prevMax = maximum up to i - 1
        # prevMin = minimum up to i - 1
        # currMax = maximum including i
        # currMin = minimum including i
        prevMax = prevMin = currMax = currMin = res = nums[0]

        for i in xrange(1, len(nums)):
            currMax = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            currMin = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            res = max(res, currMax)
            prevMax = currMax
            prevMin = currMin
        return res
