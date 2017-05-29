"""
LC 34 Search for a range
Go through twice, find the first target
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        res = list()
        start = self.findFirstTarget(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, self.findFirstTarget(nums, target + 1) - 1]

    def findFirstTarget(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i + 1 < j:
            mid = i + (j - i) / 2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid
        if nums[j] < target:
            return j + 1
        if nums[i] >= target:
            return i
        return j
