"""
问题：输入一个int x，找到他的sqrt
思路：二分法
1. 初始值start = 1, end = x 不要错把start初始为0
2. 正常二分
3. 出loop后，查看end * end <= x，返回end，不行就返回start
完成
"""

class Solution(object):
    def mySqrt(self, x):
        if x is None or x == 0:
            return 0
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
