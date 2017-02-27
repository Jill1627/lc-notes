class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hsmap = dict()


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        # hsmap: key as number, value as occurence
        if number in self.hsmap:
            self.hsmap[number] += 1
        else:
            self.hsmap[number] = 1

    def find(self, target):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.hsmap:
            other = target - num
            # after and, handles what if other == num
            if other in self.hsmap and (other != num or self.hsmap[num] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
