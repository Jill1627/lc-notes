"""
思路：从罗马字符串的后往前
1. 字典中一一对应罗马数字与阿拉伯数字
2. 需要两个初始值：sum = 最后一位罗马数字对应的int 和index 从倒数第二位开始
3. 如果当前index比index+1位的数字小，则减法（罗马数字九是IX）
4. 如果当前index增大了，则为正常加法
5. 每轮index往前移一位
"""

class Solution(object):
    def romanToInt(self, s):
        Roman = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
        }
        if s == "":
            return 0
        index = len(s) - 2
        sum = Roman[s[-1]]
        while index >= 0:
            if Roman[s[index]] < Roman[s[index + 1]]:
                sum -= Roman[s[index]]
            else:
                sum += Roman[s[index]]
            index -= 1
        return sum

""" own solution: basically the same as above """
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = dict()
        lookup['I'] = 1
        lookup['V'] = 5
        lookup['X'] = 10
        lookup['L'] = 50
        lookup['C'] = 100
        lookup['D'] = 500
        lookup['M'] = 1000

        val = lookup[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if lookup[s[i]] < lookup[s[i + 1]]:
                val -= lookup[s[i]]
            else:
                val += lookup[s[i]]
        return val
