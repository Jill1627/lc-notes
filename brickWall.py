"""
LC 554 Brick Wall
Question: given a 2d matrix, each row diff lens, find a place to cut through vertically to encounter the least number of bricks

Idea: use a hashmap <prefix sum of each row : count of times it appears> - impossible within the same row, so when a same prefix sum appears, must be across different rows and bricks end at same index

Steps:
1. Initialize: hashmap, maxSync variable to keep track of maximum number of bricks ending at same index, so that when cut through, no through middle of bricks
2. Loop: each row, each brick within a row, increment rowSum (prefix sum), update hashmap, whenever a same sum appears, update maxSync
3. result is number of rows - maxSync
"""

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # legal check
        if wall is None or len(wall) == 0 or len(wall[0]) == 0: return 0

        # initialize
        hm = dict() # hashmap <prefix sum of each row : count of times it appears>
        maxSync = 0
        # loop
        for row in wall:
            rowSum = 0
            for i in xrange(len(row) - 1):
                rowSum += row[i]
                if rowSum not in hm:
                    hm[rowSum] = 1
                else:
                    hm[rowSum] += 1
                maxSync = max(maxSync, hm[rowSum])
        return len(wall) - maxSync
