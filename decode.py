"""
题目：将字母a-z对应数字1-26，问给一个数字strings，有多少种字母排列可能性
思路：动态规划
1. 用一个function装到目前为止的排列方式
2. prev, curr表示之前和当前的研究数字对象
3. f[i+1]为对应i位置的数字
4. 需要考虑的情况分为
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        n = len(s)
        res = [0] * (n + 1)
        res[-1] = 1
        res[-2] = 0 if s[-1] == '0' else 1
        for i in range(len(res) - 3, -1, -1):
            if s[i] == '0':
                continue
            if int(s[i : i + 2]) <= 26:
                res[i] = res[i + 1] + res[i + 2]
            else:
                res[i] = res[i + 1]
        return res[0]
