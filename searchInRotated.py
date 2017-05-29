"""
LC. 33 Search in Rotated Sorted Array
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]: # first half continuous
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else: # second half continuous
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
