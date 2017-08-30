"""
LC 76 Minimum Window Substring
Sliding window with two pointers: O(n)

Steps:
1. loop through target string to record its chars and each char's occurence in hm [char : number of this char needed to be matched (occurrence)]
2. loop through source string and maintain hmT and count variable
3. If a char in s matches, decrement hmT and count variable accordingly
4. when count equals to the length of t, meaning t is fully matched: 1) see if current substring is shorter than minimum length; 2) try move forward left pointer, maintain hmT and count variable also
"""

""" Solution 1: Better space complexity
One hashmaps key = char value = # of this char for String T needed to be matched """
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None: return ""
        if len(s) < len(t): return ""

        hmT = dict() # hashmap key = char in T, value = occurrence of char in T
        count = 0 # count of chars in S that match chars in T
        j = 0 # left index of window in S
        minLen = len(s) + 1 # minimum size of window
        res = ""

        for i in xrange(len(t)):
            if t[i] in hmT:
                hmT[t[i]] += 1
            else:
                hmT[t[i]] = 1

        for i in xrange(len(s)): # i = right index of window
            if s[i] in hmT:
                hmT[s[i]] -= 1 # decrement char occurence once match
                if hmT[s[i]] >= 0: # means that this char s[i] is used for matching, it is not excessive char (i.e. 3rd k if only 2 k in t)
                    count += 1
                while count == len(t): # try move forward left pointer
                    currLen = i - j + 1
                    if currLen < minLen:
                        minLen = currLen
                        res = s[j : i + 1]
                        # print "minLen = " + str(minLen) + " res = " + res
                    if s[j] in hmT: # if left pointer char also in t
                        hmT[s[j]] += 1
                        if hmT[s[j]] > 0: # if t is not fully matched
                            count -= 1
                    j += 1
        return res



""" Solution 2: 2 hashmaps key = char value = occurrence for both S and T
1. initialize hashmap T
2. loop through s: maintain hashmap S
3. Maintain count variable
4. When count == len(t) - t is fully matched
5. Try forward left pointer
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None or len(s) < len(t) : return ""

        hmS = dict()
        hmT = dict()
        count = 0
        j = 0
        start = -1
        minLen = len(s) + 1

        # initialie hmT
        for i in xrange(len(t)):
            if t[i] in hmT:
                hmT[t[i]] += 1
            else:
                hmT[t[i]] = 1

        # start looping s
        for i in xrange(len(s)):
            # maintain hmS
            if s[i] in hmS:
                hmS[s[i]] += 1
            else:
                hmS[s[i]] = 1
            # maintain count
            if s[i] in hmT and hmS[s[i]] <= hmT[s[i]]:
                count += 1
            # maintain left pointer when  whole T is matched
            if count == len(t):
                # left pointer increments 2 cases: 1) this char not in t; 2) S has more than T needs
                while s[j] not in hmT or hmS[s[j]] > hmT[s[j]]:
                    if s[j] in hmT:
                        hmS[s[j]] -= 1
                    j += 1
                # compare current window size with minimum window size
                currLen = i - j + 1
                if currLen < minLen:
                    minLen = currLen
                    start = j

        if start > -1:
            return s[start : start + minLen]
        return ""
