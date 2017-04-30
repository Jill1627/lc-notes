""" LC 243 Shortest Word Distance """

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if words is None or len(words) == 0:
            return 0
        pos1 = -1
        pos2 = -1
        minDist = len(words) - 1
        for i in xrange(len(words)):
            if words[i] == word1:
                pos1 = i
            elif words[i] == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                minDist = min(minDist, abs(pos1 - pos2))
        return minDist
