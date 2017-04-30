""" Quick Sort """
def quickSort(self, nums):
    toSort = list(nums)
    if nums is None or len(nums) == 0:
        return nums
    sortRange(0, len(nums), toSort)

def sortRange(start, last, nums):
    
