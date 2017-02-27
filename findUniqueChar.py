class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        hashmap = dict()
        for c in slist:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        for i in range(len(slist)):
            if hashmap[slist[i]] == 1:
                return i
        return -1
