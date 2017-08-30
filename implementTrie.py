"""
LC 208 Implement Trie
Idea: implement an inner class TrieNode, with fields children hashmap, and isWord boolean

Steps:
1. constructor with a TrieNode as root
2. insert operation: search each char in word, whenever encountering a null child node, create new and add it to parent node's children hashmap
3. search operation: search each char in word, whenever not found (null) False
"""

class TrieNode(object):

    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if node is None:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)\
