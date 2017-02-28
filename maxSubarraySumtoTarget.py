# LC 325
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumMap = dict()
        total = 0
        longest = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sumMap: # if it's a new sum, add to map
                sumMap[total] = i
            if total == k: # now check: if total equals target, update longest
                longest = i + 1
            elif total - k in sumMap: # if a later sum - a previous sum == K! found a subarray from i_prev to i_latter
                longest = max(longest, i - sumMap[total - k])
        return longest
