"""
LC 525 Contiguous Array - find the maximum length of subarray that have equal amount of 0 and 1

Idea: hashmap, use -1 to represent 0, and 1 to represent 1, whenever there are equal number of 0 and 1, the sum will be 0

Steps:
1. Initialize:
use a hashmap <prefixSum : index>, prefixSum, maxLen, give the map an initial value of indexMap[0] = -1 meaning that a prefixSum = 0 has an index of -1 to start with
2. Loop:
update prefixSum, +1 if it's a 1, -1 if it's a zero
check in hm: if prefixSum already in, meaning from prev index to this index, prefixSum increment = 0, equal number of 0 and 1 is found -> update maxLen
otherwise, add it to hm
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        # initialize
        indexMap = dict()
        prefixSum = 0
        maxLen = 0
        indexMap[0] = -1
        # loop
        for i in xrange(len(nums)):
            prefixSum += 1 if nums[i] == 1 else -1
            if prefixSum in indexMap:
                maxLen = max(maxLen, i - indexMap[prefixSum])
            else:
                indexMap[prefixSum] = i
        return maxLen
