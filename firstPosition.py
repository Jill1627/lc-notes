"""
问题：寻找一条sorted array中的target第一次出现的index
思路：二分法
Key：根据第一次出现，合理调整end & start的移动
"""

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            if nums[mid] < target:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
