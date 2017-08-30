# LC 325 max subarray length sum up to k
"""
Idea:
Use hashmap to store - key: cumulative sum from index 0, value: index i or any previous index that sums up to this cumulative sum
Whenever a total - k exists in the hashmap, indicating that k is the difference between current total and some previous sum, update longest

Steps:
1. Initialize: sumMap[prefix sum : index], sumMap[0 : -1], total - running total, longest - result
2. Loop: whenever a (total - k) exists in the map, k = difference between two existing prefix sum
"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        sumMap = dict()
        sumMap[0] = -1 # initialize pos index to sum to zero
        # hashmap key: cumulative sum from index 0 to index i, value: index i or smallest index that sums up to that sum
        total = 0
        # a cumulative sum from index 0 up to index i
        longest = 0
        # longest subarray length
        for i in xrange(len(nums)):
            total += nums[i]
            if total not in sumMap:
                sumMap[total] = i
            # if total already in sumMap, current i is not going to give longest subarray because there some previous index that also sums up to this total
            if total - k in sumMap:
                longest = max(longest, i - sumMap[total - k])
        return longest


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumMap = dict()
        total = 0
        longest = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sumMap: # if it's a new sum, add to map
                sumMap[total] = i
            if total == k: # now check: if total equals target, update longest
                longest = i + 1
            elif total - k in sumMap: # if a later sum - a previous sum == K! found a subarray from i_prev to i_latter
                longest = max(longest, i - sumMap[total - k])
        return longest
