"""
Tag：Facebook，Easy
问题：在数组中寻找两个数使得他们之和等于目标target
思路：使用dictionary(hashTable)来存每一个数值的“另一半”
     Key: target - nums[i] Value: i
"""

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            else:
                map[target - nums[i]] = i
        return [-1, -1]
