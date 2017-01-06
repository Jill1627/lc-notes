"""
问题：在一个大到无法估计size的sorted array，寻找target，返回第一个index
思路：二分法
Key：用index来寻找end,start with index = 0,不断x2 + 1来找到一个包含了target的end point
"""

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1
        start = 0
        end = index + 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
