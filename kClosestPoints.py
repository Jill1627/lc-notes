"""
Solution 1: make heap of size K and collect points by minimal distance O(NLogK) complexity.

Solution 2: Take an array of size N and Sort by distance. Should be used QuickSort. As answer take first K points. This is too NlogN complexity but it is possible optimize to approximate O(N). If skip sorting of unnecessary sub arrays. When you split array by 2 sub arrays you should take only array where Kth index located. complexity will be : N +N/2 +N/4 + ... = O(N).

Solution 3: search Kth element in result array and takes all point lesser then founded. Exists O(N) alghoritm, similar to search of median. - Quick select
"""

class Solution(object):
    def findCrossOver(self, nums, low, high, x):
        # do binary search to find cross over

    def getKclosest(self, x, k, n):
        left = self.findCrossOver(nums, 0, n - 1, x)
        right = left + 1
        count = 0
        res = []
        if nums[left] == x: left -= 1
        while left >= 0 and right <= n and count < k:
            if abs(x - nums[left]) < abs(x - nums[right]):
                res.append(nums[left])
                left -= 1
            else:
                res.append(nums[right])
                right += 1
            count += 1
        while count < k and left >= 0:
            res.append(nums[left])
            left -= 1
            count += 1
        while count < k and right < n:
            res.append(nums[right])
            right += 1
            count += 1
