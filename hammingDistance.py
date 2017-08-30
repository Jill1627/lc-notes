"""
LC 461 Hamming Distance
Count the number of bits which are different
"""
# Strategy: x XOR y, and count the 1 bits
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        oneBit = 0
        while diff > 0:
            if diff % 2 == 1:
                oneBit += 1
            diff /= 2
        return oneBit

# A more concise way of XOR + counting bits
class Solution(object):
    def hammingDistance(self, x, y):
        diff = x ^ y
        return bin(diff).count("1")

# A different way to count bits
class Solution(object):
    def hammingDistance(self, x, y):
        diff = x ^ y
        ones = 0
        while diff:
            ones += 1
            diff &= diff - 1
        return ones
