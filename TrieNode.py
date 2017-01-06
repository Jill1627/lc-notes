"""
问题：implement Trie: __init__, insert, search, startsWith

"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            current = current.children[char]
        current.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            current = current.children.get(char)
            if current is None:
                return False
        return current.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if current is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
