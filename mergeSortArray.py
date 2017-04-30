""" Merge sort array """
def mergeSort(self, nums):
    if nums is None or len(nums) == 0:
        return nums
    return self.divideThenMerge(0, len(nums) - 1, nums)

def divideThenMerge(self, start, end, nums):
    if start >= end:
        return list(nums[start])

    mid = start + (end - start) / 2
    left = self.divideThenMerge(start, mid, nums)
    right = self.divideThenMerge(mid + 1, end, nums)

    merged = list()
    i, j= 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
    while j < len(right):
        merged.append(right[j])
