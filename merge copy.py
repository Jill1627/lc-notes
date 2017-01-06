"""
问题：将nums2并入nums1，两个数组都是升序，nums1有足够空间
思路：从后往前遍历，三个指针i,j,index
1. while i,j都从后往前，没到最前
2. 比大小，谁大谁进入nums1[index]
3. 注意更新i, j, index
4. 别忘了剩余的i, or j
完成
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if nums1 is None or len(nums1) == 0:
            return
        if nums2 is None or len(nums2) == 0:
            return
        index = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1
        while i >= 0:
            nums1[index] = nums1[i]
            index -= 1
            i -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1
        return
