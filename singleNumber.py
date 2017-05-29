"""
LC.136 Single number
No extra space, also ok to use XOR
"""


""" My own solution with O(1) space with set """
from sets import Set
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        once = Set()
        for i in nums:
            if i not in once:
                once.add(i)
            else:
                once.remove(i)
        return next(iter(once))
