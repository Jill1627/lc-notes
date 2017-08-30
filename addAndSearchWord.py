"""
LC211 Add and search word
Idea: Use Trie - built-in class TrieNode

Steps:
1. Add word: like add word in Trie
2. Search word: use recursion to handle both alpha and dot cases
- base case: when position k equals length of num, reaching the end, check isWord
- if alpha, check itself, and enter recursion for next char
- if dot, don't need to check current, just enter recursion to loop through each child of this parent

helper method is used to check whether this char at current position in trie

"""

class TrieNode(object):
        def __init__(self):
            self.children = dict()
            self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        parent = self.root
        for c in word:
            child = parent.children.get(c)
            if child is None:
                child = TrieNode()
                parent.children[c] = child
            parent = child
        parent.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, k, parent):
        if k == len(word): return parent.isWord
        # case: char is NOT a dot
        if word[k] != '.':
            return word[k] in parent.children and self.searchHelper(word, k + 1, parent.children[word[k]])
        else:
            for c in parent.children:
                    if self.searchHelper(word, k + 1, parent.children[c]):
                        return True
            return False






# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
