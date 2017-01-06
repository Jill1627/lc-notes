"""
问题：输入一个数列，寻找下一个排列（大一格）
思路：分三步
1. 从后往前遍历，发现第一个下降的i （135432中的3 = nums[1]）
2. 从最后往前至i，寻找刚好比nums[i]大一格的nums[j] （nums[3]的4），交换i和j
3. 将i+1至最后的数列逆转，从降序变为升序 (145332 --> 142335即最终答案)
完成
"""

class Solution(object):
    def nextPermutation(self, nums):
        if nums is None:
            return
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i--
        if i < 0: "important corner case: len == 0 or 1"
            nums.reverse()
            return
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i + 1 :] = reversed(nums[i + 1 :])
