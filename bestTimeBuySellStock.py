class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        maxProfit = 0
        buyPrice = prices[0]
        for price in prices:
            buyPrice = min(buyPrice, price)
            maxProfit = max(maxProfit, price - buyPrice)
        return maxProfit
