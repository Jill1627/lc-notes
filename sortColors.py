"""
题目：将三个颜色，0，1，2排序
思路：三个指针，高，低，和当前
1. 遇到==2，就与hi交换，hi--
2. 遇到==0，就与lo交换，lo++
3. 到最后所有1都聚集在中间
完成
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in place
        """
        if nums is None or len(nums) == 0:
            return
        lo = 0
        hi = len(nums) - 1
        for i in xrange(len(nums)):
            """
            Pay attention to 3 things:
            1. Use a while loop not an if
            2. Check i < hi before entering loop
            3. Swap with right first, then swap with left
            """
            while nums[i] == 2 and i < hi:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            while nums[i] == 0 and i > lo:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
