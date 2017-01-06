"""
问题：给一个array，里面是木段的长度，给一个木段个数，求最长的切割长度
思路：二分法
Steps：
1.二分的最短木段长度为1，最长为max(L)，也就是最长的那一段
2. 每一个mid，都计算一下numberOfPieces can be produced，和目标k比较
"""

class Solution:
    """
    :type L: array
    :type k: int
    :rtype: int
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
        start = 1
        end = max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            numberOfPieces = sum([l / mid for l in L])
            if numberOfPieces >= k:
                start = mid
            else:
                end = mid
        if sum(l / end for l in L) >= k:
            return end
        return start
