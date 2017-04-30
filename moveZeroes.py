# LC283 FB
""" Two pointers """

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return
        firstZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[firstZero], nums[i] = nums[i], nums[firstZero]
                firstZero += 1
