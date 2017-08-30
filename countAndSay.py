"""
问题：输出第n位count and say sequence - 注意count and say sequence的生成方式
思路：递归，算法设计如何从n-1到n
1. 考虑n=0，1的特殊情况
2. 初始：res, count = 1, prev = self.countAndSay(n - 1),还有prevNum
3. 在loop中，考察当前i(curNum)与prevNum的关系，更新count
4. 如果当前位与前一位相等，只需要count++
5. 如果当前位与前一位不等，更新答案，同时：reset count = 1，preNum = curNum
6. 最后一步，还要将prevNum加入答案
完成
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # base case
        if n is None or n == 0:
            return "0"
        if n == 1:
            return "1"
        # recursion
        prev = self.countAndSay(n - 1)
        prevNum = prev[0]
        count = 1
        res = ""
        for i in xrange(1, len(prev)):
            if prev[i] == prevNum:
                count += 1
            else:
                res = res + str(count) + prevNum
                prevNum = prev[i]
                count = 1
        res = res + str(count) + prevNum
        return res
