"""LC128 Longest Consecutive Sequence - #array, #hashmap """
# Google, #facebook, #hard

""" HashMap"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        hm = dict()
        for n in nums:
            if n in hm: continue
            # leftLen is n - 1's seq length
            leftLen = hm[n - 1] if n - 1 in hm else 0
            # rightLen is n + 1's seq length
            rightLen = hm[n + 1] if n + 1 in hm else 0

            currLen = leftLen + rightLen + 1
            hm[n] = currLen

            maxLen = max(maxLen, currLen)
            # update the two ends of this sequence
            hm[n - leftLen] = currLen
            hm[n + rightLen] = currLen


        return maxLen

""" tricky smart Solution """
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
