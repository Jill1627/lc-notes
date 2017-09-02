"""
LC 85 Maximal Rectangle [hard]
Idea: dp
See inline comment
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # initialize
        n = len(matrix)
        m = len(matrix[0])
        left = [0] * m # contains data about effective left boundary from previous row
        right = [m] * m # contains data about effective right boundary from previous row
        height = [0] * m
        currLeft = 0 # contains data about effective left boundary at current row
        currRight = m # contains data about effective right boundary at current row
        maxArea = 0

        # loop
        for i in xrange(n):

            # update height
            for j in xrange(m):
                if matrix[i][j] == '1':
                    height[j] += 1 # increment height
                else:
                    height[j] = 0 # if matrix[i][j] is 0, reset height

            # update left
            currLeft = 0
            for j in xrange(m):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], currLeft) # update curr left[j] with an effective left boundary
                else:
                    currLeft = j + 1 # update curr row's effective left boundary, for prep next '1' occurrence
                    left[j] = 0 # reset effective left boundary to 0 when sees a 0, as it is useless forming rectangle now

            # update right
            currRight = m
            for j in xrange(m - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], currRight) # update curr right[j] with an effective right boundary
                else:
                    currRight = j # update curr row's effective right boundary for next '1' occurrence
                    right[j] = m # reset effective right boundary to m
                    
            # update maxArea
            for j in xrange(m):
                currArea = height[j] * (right[j] - left[j])
                maxArea = max(maxArea, currArea)

        return maxArea
