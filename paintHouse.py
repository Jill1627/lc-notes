""" LC256 Paint House """
""" Subproblem, costs[i][j] = min cost of painting up to house i with color j"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None or len(costs) == 0:
            return 0
        n = len(costs)
        for i in xrange(1, n):
            # Use original matrix directly, update o it
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[n - 1][0], costs[n - 1][1], costs[n - 1][2])