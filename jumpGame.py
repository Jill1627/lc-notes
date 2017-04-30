"""Greedy solution - O(n)"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return True
        n = len(nums)
        far = nums[0]
        for i in range(n):
            if i > far: return False
            far = max(far, i + nums[i])
        return True




""" DP solution - O(n^2) """
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return True
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True
        j = 0
        for i in range(n):
            if reachable[i]: continue
            else:
                reachable[i] = reachable[j] and nums[j] >= i - j
        return reachable[n - 1]
