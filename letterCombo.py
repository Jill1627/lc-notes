"""
题目：LC17: 根据电话数字字符串，输出所有字母组合
思路：三个For循环，依次为，每一个数字，每一个数字相对应的字母，如果答案已有内容，每一个答案elem
1. 初始化chars list包含所有字母组，res记录答案
2. 循环每一个数字时：用num存储，temp暂存目前答案
3. 循环每一个字母时：看答案是否有内容，如无，直接加入temp
4. 如果已有内容，要循环每一个现有答案elem，逐个加入当前字母
5. 最终，将temp替换成答案
完成
"""

"""Later solution, easier to understand """
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if digits is None or len(digits) == 0: return []
        res = [""]
        for d in digits:
            chars = lookup[int(d)]
            temp = list()
            for c in chars:
                for r in xrange(len(res)):
                    temp.append(res[r] + c)
            res = temp
        return res


class Solution(object):
    def letterCombo(self, digits):
        chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(len(digits)):
            num = digits[i]
            temp = []
            for j in range(len(chars[num])):
                if len(res):
                    for k in range(len(res)):
                        temp.append(res[k] + chars[num][j])
                else:
                    temp.append(str(chars[num][j]))
            res = copy.copy(temp)
        return res
