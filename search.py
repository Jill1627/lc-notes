"""
问题：在一个扭转了的数组中寻找目标数字
思路：用二分法，分情况讨论(画图很重要)
1. 两种情况的扭转分开考虑：扭转点在后半部分，扭转点在前半部分
2. 情况一：目标如果在连续部分（前半）则end=mid,反之，则start = mid
3. 情况二：目标如果在连续部分（后半）则start-mid, 反之，则end = mid
4. 出了while之后，分别考察start, end是否是target。最终，return -1为没找到
完成
"""

class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if (nums[mid] == target):
                return mid
            if (nums[start] < nums[mid]):
                if (nums[start] <= target and target <= nums[mid]):
                    end = mid
                else:
                    start = mid
            else:
                if (nums[mid] <= target and target <= nums[end]):
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
