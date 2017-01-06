"""
问题：在source字符串中寻找target字符串
思路：对source的每个字符进行遍历，遍历过程中，遍历target字符串
1. 遍历source的每个字符，注意范围：从0到lenS - lenT + 1即可，超过此范围后面剩下不到一个T
2. 遍历target的每个字符，一旦source[i+j]和target[j]对应不上，break，其他情况j++
3. 出target遍历时，比较j和target长度，如相等，说明找到，回复此时i的位置
4. 其他所有情况，为未找到，-1
完成
"""

class Solution(object):
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        lenS = len(source)
        lenT = len(target)
        for i in range(lenS - lenT + 1):
            j = 0
            while (j < lenT):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == lenT:
                return i
        return -1
