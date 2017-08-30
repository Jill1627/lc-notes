"""
LC 157 Read N characters given Read4 API
Weird questions
See comments in line
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # initialize
        eof = False
        total = 0
        tempBuffer = [0] * 4

        while not eof and total < n:
            # try reading using read4 api
            count = read4(tempBuffer)

            # check if eof
            if count < 4: eof = True
            # get legal count with check of n char bound
            count = min(count, n - total)

            for i in xrange(count):
                buf[total] = tempBuffer[i]
                total += 1
        return total
