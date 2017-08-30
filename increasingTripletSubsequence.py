"""
LC 334 Increasing triplet subsequence
Idea: section number range to update small and medium, once large is found, return True

See in-line comment
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # initialize, use small - medium - large
        if nums is None or len(nums) == 0:
            return False
        # initialize small and medium with largest possible value
        small = max(nums) + 1
        medium = max(nums) + 1
        for n in nums:
            if n <= small: # n is the smallest so far
                small = n # let n be the small candidate
            elif n <= medium: # n is greater than small, but less than medium
                medium = n # let n be medium candidate
            else: # n is greater than medium, and we already have medium greater than small, here is our triplet found
                return True
        return False
