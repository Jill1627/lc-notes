# LC300 Longest increasing subsequence LIS Microsoft


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = [0] * len(nums)
        for i in range(len(nums)):
            curMax = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = length[j] + 1
                    curMax = max(curr, curMax)
            length[i] = curMax
        return max(length)
