"""
问题：在扭转的排序数组中寻找最小值
思路：用pivot point来当target比较大小
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        pivot = nums[end]
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= pivot:
                end = mid
            else:
                start = mid
        if nums[start] <= nums[end]:
            return nums[start]
        return nums[end]
