""" LC 244 Shortest Word Distance II """

class WordDistance(object):


    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hm = dict()
        for i, word in enumerate(words):
            self.hm[word] = self.hm.get(word, []) + [i]


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(i1 - i2) for i1 in self.hm[word1] for i2 in self.hm[word2])

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
