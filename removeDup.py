"""
问题：sorted array去重，可允许up to 2 copies
思路：two pointers
1. 遍历每一个元素，size 2以内，直接更新
2. 如果当前元素比nums[size-2]不同，则更新，size++
完成
"""

class Solution(object):
    def removeDup(self, nums):
        """
        type nums: list[int]
        rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        size = 0
        for num in nums:
            if size < 2 or num > nums[size - 2]:
                nums[size] = num
                size += 1
        return size
