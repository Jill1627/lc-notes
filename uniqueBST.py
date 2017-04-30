class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Define "number of unique bst of n sequence" N(n)
        # Define "number of unique bst rooted at i" R(i, n)
        # N(n) = R(1, n) + R(2, n) + ... + R(n, n) meaning N(n) equals to the sum of R rooted at 1, 2, 3, ...n
        # R(1, n) = N(0) * N(n - 1) => R(i, n) = N(i - 1) * N(n - i)
        # N(n) = N(0) * N(n - 1) + N(1) * N(n - 2) + ... + N(n - 1) * N(0)
        N = [0] * (n + 1)
        N[0] = 1
        N[1] = 1
        for i in range(2, n + 1): # sequence of i
            for j in range(1, i + 1): # rooted at j
                N[i] += N[j - 1] * N[i - j]
        return N[n]
