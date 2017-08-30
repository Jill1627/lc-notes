"""
LC 49 Group anagrams
Idea: use hashmap [sorted anagram for the group : list of anagrams within same group]

steps:
1. loop through the list of word
2. for each word, get its sorted alphabetically, see if it's in hashmap
Intuitive
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) == 0: return []

        res = list()
        hm = dict()

        for word in strs:
            sortedCharList = sorted(word)
            sortedStr = ''.join(sortedCharList)
            if sortedStr not in hm:
                hm[sortedStr] = list()
            hm[sortedStr].append(word)
        for item in hm:
            res.append(hm[item])
        return res
