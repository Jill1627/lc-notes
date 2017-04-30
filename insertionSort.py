""" Insertion Sort """
def insertionSort(self, nums):
    if nums is None or len(nums) == 0:
        return
    size = len(nums)
    for curr in xrange(1, size):
        runner = curr - 1
        while runner >= 0 and nums[runner] < nums[curr]:
            nums[runner], nums[curr] = nums[curr], nums[runner]
            runner -= 1
            curr -= 1
