"""
问题：输入数组nums, 要求去掉重复元素，输出最终长度int
思路：简单two pointers，newSize指向目前最新的元素，一旦nums[i]!=nums[newSize],更新newSize及nums[newSize]
"""

class Solution(object):
    def removeDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        newSize = 0
        for i in range(len(nums)):
            if (nums[i] != nums[newSize]):
                newSize += 1
                nums[newSize] = nums[i]
        return newSize + 1
