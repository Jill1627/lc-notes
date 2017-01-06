"""
问题：输入一个string，含大小写，空格，和数字，判断是否为palindrome,大写字母和小写字母视为一致，空格不用对齐
思路：从两头往中间遍历，考虑两种更新的情况
1. 如果遇到非字母及非数字的情况，即空格，直接跳过看下一个
2. 如果遇到字母不相等（比较前先化为小写），return False，其他return True
完成
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if lo < hi and not s[lo].isalpha() and not s[lo].isdigit():
                lo += 1
            elif lo < hi and not s[hi].isalpha() and not s[hi].isdigit():
                hi -= 1
            else:
                if s[lo].lower() != s[hi].lower():
                    return False
                lo += 1
                hi -= 1
        return True
