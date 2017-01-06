"""
问题：输入: String word, 2D array, board,要求输出board中能否连出一个word，连接方法是上下左右可走
思路：DFS
1. 特殊情况先考虑，word长度为0，直接return true，board不存在，直接return false
2. 遍历board的从上到下，从左到右每一个元素，都进行DFS(private method)
3. DFS中，特殊情况先考虑：如果word长度为0了，直接return true；如果i，j超出边界了，直接return false；如果board[i][j] != word[0]，直接return false；综上何为一句
4. 接下来进行recursion，先把board[i][j]记录下来=‘#’; recurse board[i][j]的上下左右
5. 每下一层，将word的第一个字母去掉, word = word[1:]
6. board[i][j]恢复
完成
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return False
        if len(word) == 0:
            return True
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False
    def dfs(self, board, word, i, j):
        if len(word) == 0:
            return True
        if  < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, word[1:], i - 1, j) or self.dfs(board, word[1:], i, j - 1) or self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i, j + 1)
        board[i][j] = temp
        return res
