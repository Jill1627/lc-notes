"""
问题：给n对左右括号，输出所有正确的括号配对方式
思路：整体运用backtracking方法递归，用helper
1. helper(left, right, tempRes, res) 针对剩余的左右括号数量
2. 如果剩余的右>左，直接return，因为不可能完全配对成功
3. 如果左右都不剩，将临时答案加入答案
4. 如果左还有剩余，进入下层递归，左剩余减一，临时答案加一个左括号
5. 右剩余，同上
完成
"""

class Solution(object):
    def generateParen(self, n):
        res = []
        if n == 0:
            return res
        helper(n, n, "", res)
        return res
    def helper(left, right, tempRes, res):
        if right > left:
            return
        if left == 0 and right == 0:
            res.append(tempRes)
        if left > 0:
            helper(left - 1, right, tempRes + "(", res)
        if right > 0:
            helper(left, right - 1, tempRes + ")", res)
