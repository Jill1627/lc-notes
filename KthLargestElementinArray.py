# LC215 Kth largest Element in an Array

""" Solution 1: time - O(NlogN) space O(1) sort first and find [k]"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) - k]


""" Solution 2: Python heapq module"""

class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
