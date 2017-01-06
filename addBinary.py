"""
题目：输入两个二进制数字的String，输出相加的结果String
思路：两个二进制字符串从后往前，逐个加
1. 初始化indexA, indexB, carry, res
2. 在while loop中，bitA就是当前位（考虑如果indexA为0了，就是0）
3. update res: 当前位的答案是bitA + bitB + carry % 2
4. update carry: (bitA + bitB + carry) / 2
5. decrement indexA 和 indexB
6. 出loop后，表示两个binary都已经遍历完，最后不要忘记考虑，还有一个进位的情况carry == 1
完成
"""

class Solution(object):
    def addBinary(self, a, b):
        indexA = len(a) - 1
        indexB = len(b) - 1
        carry = 0
        res = ""
        while indexA >= 0 or indexB >= 0:
            bitA = int(a[indexA]) if indexA >= 0 else 0
            bitB = int(b[indexB]) if indexB >= 0 else 0
            if (bitA + bitB + carry) % 2 == 0:
                res = "0" + res
            else:
                res = "1" + res
            carry = (bitA + bitB + carry) / 2
            indexA -= 1
            indexB -= 1
        if carry == 1:
            res = "1" + res
        return res
