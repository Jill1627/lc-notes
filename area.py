"""
问题：求两个长方形的总面积
思路：查看上下左右四个边界，看两个长方形是否有交界
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = 0
        rec1 = (C - A) * (D - B)
        rec2 = (G - E) * (H - F)

        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)

        if left < right and top > bottom:
            overlap = (right - left) * (top - bottom)

        return rec1 + rec2 - overlap
