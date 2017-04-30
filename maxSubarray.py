# LC 53 Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = list()
        if nums is None or len(nums) == 0:
            return res
        res.append(nums[0])
        for i in range(1, len(nums)):
            if res[i - 1] < 0:
                res.append(nums[i])
            else:
                res.append(nums[i] + res[i - 1])
        return max(res)


""" My own solution """
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        maxSum = [0 for i in xrange(len(nums))]
        maxSum[0] = nums[0]
        res = nums[0]

        for i in xrange(1, len(nums)):
            if maxSum[i - 1] >= 0:
                maxSum[i] = maxSum[i - 1] + nums[i]
            else:
                maxSum[i] = nums[i]

        return max(maxSum)
