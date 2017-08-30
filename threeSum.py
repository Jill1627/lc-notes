"""
问题：在一个数组中寻找三个数，相加之和等于0
思路：循环每一个i，从第0个到倒数第三个，对每个i，都有后面的lo，hi
1. 先升序排列，初始长度length，和答案result
2. for每个i：第一件事，去重，初始target = 0 - nums[i]
3. 然后再寻找nums[lo] + nums[hi] == target的lo，hi，append到答案
4. 过程中仍然需要对lo和hi去重
5. 如果不是==target，如果<，lo增加1，如果>，hi减小1，因为已排序
6. 完成
"""

'''Clearer solution '''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        if nums is None or len(nums) < 3:
            return res

        nums.sort()

        for i in xrange(len(nums) - 2):
            # outter if statement to remove duplicate
            if i == 0 or nums[i - 1] != nums[i]:
                lo = i + 1
                hi = len(nums) - 1
                target = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[lo], nums[hi]])
                        # also removes duplicate at lo and hi
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1
        return res


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length - 2):
            "Avoid duplicate"
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            lo, hi = i + 1, length - 1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    "Avoid duplicate"
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    "Avoid duplicate"
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1
        return result
