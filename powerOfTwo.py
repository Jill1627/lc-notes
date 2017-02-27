#LC 231 Power of two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n % 2 == 0:
            n /= 2
        return n == 1


""" bit operation """
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        return not (n & (n - 1))
