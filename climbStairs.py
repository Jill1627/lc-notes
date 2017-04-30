"""LC70 Climbing Stairs """
"""Fibonacci recur -> Dynamic Programming -> 2 variable array """

# My own solution
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return 0
        if n == 0 or n == 1:
            return 1
        prev = 1
        curr = 1
        for i in xrange(2, n + 1):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr

# same thing, but harder to understand
class Solution(object):
    def climbStairs(self, n):
        if n<= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step_before = 2
        two_step_before = 1
        res = 0
        for i in range(2, n):
            res = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = res
        return res
