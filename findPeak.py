"""
问题：输入一个数组，找到其中任何一个峰值，输出index
思路：二分法
1. 如果mid在下降，end过来；如果mid在上升，start过来
2. 最后看答案是start还是end
完成
"""
class Solution(object):
    def findPeak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        "Using binary search"
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            "mid is on descending, left of it is higher"
            if nums[mid] < nums[mid - 1]:
                end = mid
            "mid is on climbing, right of it is higher"
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return end
        else:
            return start
