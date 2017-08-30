"""
Idea:
Use 1-d array dp
Each time, look at a substring of 2 chars, and check its number range, total of 4 cases
1. if subNum is within range: [11, 26]: from 1 char before or 2 chars before
2. if subNum is 10 or 20: only from 2 chars before
3. if subNum does not end with 0: from 1 char before
4. all the rest: no way to decode (i.e. 01, 40): return 0


题目：将字母a-z对应数字1-26，问给一个数字strings，有多少种字母排列可能性
思路：动态规划
1. 用一个function装到目前为止的排列方式
2. prev, curr表示之前和当前的研究数字对象
3. f[i+1]为对应i位置的数字
4. 需要考虑的情况分为
"""

""" A clearer solution -  将数轴根据0, 1 - 9, 10, 11-26, 20, and else 分段处理"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0 or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2, len(s) + 1):
            sub = s[i - 2 : i]
            if 10 < int(sub) <= 26 and int(sub) != 20:
                dp[i] = dp[i - 1] + dp[i - 2]
            elif int(sub) == 10 or int(sub) == 20:
                    dp[i] = dp[i - 2]
            elif int(s[i - 1]) != 0:
                    dp[i] = dp[i - 1]
            else:
                return 0
        return dp[len(s)]


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
