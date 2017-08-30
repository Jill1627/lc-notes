"""
LC 269 Alien Dictionary
Idea: topological sorting on chars

Steps:
1. Initialize: use a hashmap [char : its in degree]; a hashmap for [char : a set of all chars that come after it lexicographically]; a queue for topsort; res
2. Add all chars to degreeMap with indegree = 0
3. Loop through all words with its prevWord, find different char, and update orderMap, break out once found
4. Topsort on degreeMap using queue, update res 
"""

from collections import deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words is None or len(words) == 0:
            return ""
        # initialize
        queue = deque()
        degreeMap = dict() # char -> indegree
        orderMap = dict() # char -> a set of its succeeding chars
        res = ""
        # 1. add each char in each word into degreeMap
        for word in words:
            for c in word:
                if c not in degreeMap:
                    degreeMap[c] = 0
        # 2. update degreeMap and orderMap
        for i in xrange(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            for j in xrange(min(len(prev), len(curr))):
                prevChar = prev[j]
                currChar = curr[j]
                if prevChar != currChar: # we know prevChar comes before currChar in lexicographical order
                    followingChars = set()
                    if prevChar in orderMap: # get prevChar's following chars set if exist
                        followingChars = orderMap[prevChar]
                    if currChar not in followingChars:
                        followingChars.add(currChar)
                        orderMap[prevChar] = followingChars
                        degreeMap[currChar] += 1
                    break # once see a different char, no need to look further
        # 3. top sort from degreeMap to create res
        for c in degreeMap:
            if degreeMap[c] == 0:
                queue.append(c)
        while queue:
            c = queue.popleft()
            res += c
            if c in orderMap:
                followingChars = orderMap[c]
                for followingChar in followingChars:
                    degreeMap[followingChar] -= 1
                    if degreeMap[followingChar] == 0:
                        queue.append(followingChar)
        print res
        print "size of dg map = " + str(len(degreeMap))
        if len(res) != len(degreeMap):
            return ""
        return res
