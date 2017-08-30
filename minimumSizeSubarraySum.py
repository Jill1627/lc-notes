"""
LC 209 Minimum size subarray sum to target (also ok to be greater than)
Idea:
2 solutions: 1. two pointers O(n); 2. binary search O(nlogn)

Steps of solution 1:
1. Initialize: use variable tempSum to keep track of current runnint sum, j as the left pointer, minLen to have full length + 1
2. loop through each num using i (right pointer), increment tempSum, as long as it's greater than target, increment left pointer j
3. update minLen if necessary
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        tempSum = 0
        minLen = len(nums) + 1
        j = 0

        for i in xrange(len(nums)):
            tempSum += nums[i]
            while tempSum >= s:
                currLen = i - j + 1
                minLen = min(minLen, currLen)
                tempSum -= nums[j]
                j += 1
        return minLen if minLen < len(nums) + 1 else 0

"""Solution 2 with binary search, needs to fix index out of bound exception """
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        # create a prefix sum array, it's already in ascending order
        prefix = list()
        prefix.append(nums[0])
        for i in xrange(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        # initialize
        minLen = len(nums) + 1
        # loop
        for i in xrange(len(nums)):
            end = self.binarySearch(i + 1, len(nums) - 1, prefix[i] + s, prefix)
            if end == len(nums): break
            minLen = min(minLen, end - i)
        return minLen if minLen < len(nums) + 1 else 0

    def binarySearch(self, start, end, target, nums):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            if nums[mid] < target:
                start = mid
        return start if nums[start] == target else end
