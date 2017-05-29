"""
问题：implement x to the power of n
思路：递归解法，每次将x的n次方，分解成一半，格外注意corner cases
1. 当n=0， 直接return 0
2. n=1，直接return x
3. 开始递归，将n次方变成 2 * half + remainder
4. 注意分情况讨论当 n<0时，输出是1/, n>0, 直接输出
完成
"""

# My dp solution
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x
        myPow = [1 for i in xrange(n + 1)]
        myPow[0] = 1
        if n > 0:
            myPow[1] = x
        for i in xrange(2, n + 1):
            myPow[i] = myPow[i / 2] * myPow[i / 2] if i % 2 == 0 else myPow[i / 2] * myPow[i / 2] * x
        return myPow[n]

# my recursive solution - potentially slow
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        half = abs(n) / 2
        remainder = abs(n) - 2 * half
        tempRes1 = self.myPow(x, half)
        tempRes2 = self.myPow(x, remainder)
        if n < 0:
            return 1 / (tempRes1 * tempRes1 * tempRes2)
        else:
            return tempRes1 * tempRes1 * tempRes2
