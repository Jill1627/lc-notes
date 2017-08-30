"""
LC 380 Insert delete getRandom
Idea: use ArrayList and hashmap
To guarantee O(1) operation, remove the last element all the time, swap if not

Steps:
1. initialize the data structure with an ArrayList nums, and a HashMap indexMap, indexMap = [num : its index in nums], initially
2. insert operation, check if it's already in, if so, return False; otherwise, add it to the end of nums, insert it into hashmap with its index in nums
3. remove operation, check if it's not in, return False if so; otherwise, check if it's the last element in the nums list, if not, swap with the last element, update indexMap for the last element, then do removal for both nums and indexMap
4. getRandom just use random.randint
"""

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.indexMap = dict()


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexMap:
            return False
        self.nums.append(val)
        self.indexMap[val] = len(self.nums) - 1 # mapping an element to its index in nums list, initially
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indexMap:
            return False

        index = self.indexMap[val]
        # swap with last element, if this val is not the last
        if index < len(self.nums) - 1:
            lastElement = self.nums[len(self.nums) - 1]
            self.nums[index] = lastElement
            self.indexMap[lastElement] = index
        self.nums.pop()
        del self.indexMap[val]
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
