"""LC128 Longest Consecutive Sequence - #array, #hashmap

2 solutions: use hashmap or hashset

Solution 1:
Idea: use a hashmap<unique num : max sequence length containing this num, if it's at boundary>

Steps:
1. Initialize: maxLen, and hashmap
2. Loop each num in nums, only considers unique ones, skip num already in hm
3. for each num, get leftLen from num - 1 and rightLen from num + 1, if not exist, get 0
4. CurrLen equals leftLen + rightLen + 1 (num itself), update maxLen if needed
5. Update this sequence's left and right boundary by updating hm[num - leftLen] and hm[num + rightLen] with currLen

Solution 2: see comments in line
"""
# Google, #facebook, #hard

""" HashMap"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        # use hashmap<unique num in nums : max sequence length containing this num, if it's at boundary>
        hm = dict()
        maxLen = 0

        for n in nums:
            # skip if n already appeared and in hm
            if n not in hm:
                leftLen = hm[n - 1] if n - 1 in hm else 0
                rightLen = hm[n + 1] if n + 1 in hm else 0
                currLen = leftLen + 1 + rightLen
                hm[n] = currLen
                # update maxLen if needed
                maxLen = max(maxLen, currLen)
                # update this sequence's left and right boundary num's sequence length
                hm[n - leftLen] = currLen
                hm[n + rightLen] = currLen
        return maxLen

""" tricky smart Solution using set """
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        maxLen = 0
        for n in nums:
            # only look at the smallest of a increasing Sequence
            # if n - 1 is in nums, n is not the smallest
            if n - 1 not in numsSet:
                incre = n + 1
                # keep increasing by 1 to see if still in nums set
                while incre in numsSet:
                    incre += 1
                # no longer in nums set, break, get the currLen
                currLen = incre - n
                maxLen = max(currLen, maxLen)
        return maxLen
