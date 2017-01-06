"""
问题：在升序array中查找target，如存在，返回index，如不存在，返回应插入的index
思路：二分法
都很简单，只要在出while loop后，考虑target与start index & end index的三个位置区间关系
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0;
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid;
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        else:
            return end + 1
