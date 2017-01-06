"""
问题：输入股价数组，卖在买之前，求最大利润
思路：记录两个值，到目前为止的最低股价minPrice, 到目前为止的最大利润maxProfit
完成
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        min_ = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - min_)
            min_ = min(min_, price)
        return maxProfit
