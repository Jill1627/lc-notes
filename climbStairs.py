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
