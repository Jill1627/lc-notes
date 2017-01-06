"""
问题：输入二维矩阵，按螺旋形顺序输出单链数组
思路：用上下左右，和方向，5个variables记录当前位置 （画图）
1. while true，分四个方向录入答案，每个方向录完后，increment
2. 每一个loop末尾，测试是否left > right or up > down，return
3. 每个loop末尾，更新direction by +1，记得module 4
"""

class Solution(object):
    def spiralMatrix(self, matrix):
        res = []
        if matrix is None or len(matrix) == 0:
            return res
        up = 0
        left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1): "别忘了+1，包含down进来"
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if left > right or up > down:
                return res
            direction = (direction + 1) % 4
