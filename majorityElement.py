"""
LC 169. Majority Element
Find the element in an array whose occurence is more then half of len(nums)
"""

""" My own solution with hashmap """
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        seen = dict()
        res = list()
        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
            if seen[n] > len(nums) / 2:
                return n

""" My own solution with bit manipulation (pseudo bit manipulation with a 2-element arra) """
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        # use key - occurence pair to keep track of most occurred element
        occur = [nums[0], 0]
        for num in nums:
            if num == occur[0]:
                occur[1] += 1
            else:
                occur[1] -= 1
                # update the mapping with current element, with occur = 1
                if occur[1] == 0:
                    occur[0] = num
                    occur[1] = 1
        return occur[0]
