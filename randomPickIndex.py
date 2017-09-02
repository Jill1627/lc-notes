"""
LC398 random pick index
Idea: based on a randomized algorithm Reservoir sampling
Steps:
1. Initialize constructor with a field: nums
2. pick operation: maintain two fields: res and count (count of targets)
3. loop trough each element of nums, only when you hit target, run a random integer between 0 and count of targets appeared, whenever it equals to 0 (probability of 1/count), update res to be current index
"""

import random
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 0
        for i in xrange(len(self.nums)):
            # only when target is found
            # generate a random number between 0 and count of target
            # rand == 0 has a probability of 1/count
            if self.nums[i] == target and random.randint(0, count) == 0:
                result = i
                count += 1
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
