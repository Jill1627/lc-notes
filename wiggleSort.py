class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i % 2 == 1 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            elif i % 2 == 0 and i != 0 and nums[i - 1] < nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
