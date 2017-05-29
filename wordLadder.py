"""
LC 127 word ladder
"""

from collections import deque
from sets import Set
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if wordList is None or len(wordList) == 0:
            return 0
        if beginWord is endWord:
            return 1
        wordList.add(beginWord)
        wordList.add(endWord)
        visited = set()
        queue = deque()
        visited.add(beginWord)
        queue.append(beginWord)
        length = 1
        while queue:
            length += 1
            qSize = len(queue)
            for i in range(qSize):
                word = queue.pop()
                for nextWord in self.getNextWord(word, wordList):
                    if nextWord in visited:
                        continue
                    if nextWord is endWord:
                        return length
                    visited.add(nextWord)
                    queue.append(nextWord)
        return 0
    def getNextWord(self, word, wordList):
        nextWords = list()
        for c in range(ord('a'), ord('z') + 1):
            for i in range(len(word)):
                if chr(c) is word[i]:
                    continue
                candidate = self.replace(word, i, c)
                if candidate in wordList:
                    nextWords.append(candidate)
        return nextWords
    def replace(self, word, index, char):
        listForm = list(word)
        listForm[index] = chr(char)
        word = "".join(listForm)
