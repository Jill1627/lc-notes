""" Selection sort """
def selectionSort(self, nums):
    if nums is None or len(nums) == 0:
        return
    size = len(nums)
    for curr in xrange(size):
        currMin = nums[curr]
        currMinIndex = curr
        for runner in xrange(curr + 1, size):
            if nums[runner] < nums[currMinIndex]:
                currMin = nums[runner]
                currMinIndex = runner
        nums[currMinIndex] = nums[curr]
        nums[curr] = currMin
