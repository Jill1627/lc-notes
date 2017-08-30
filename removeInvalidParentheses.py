"""
LC301 Remove invalid parentheses
Idea: BFS - guarantee whenever a valid is found, it must be the minimum removal
helper method as valid parentheses

Steps:
1) Initialize queue for bfs
2) Setup boolean flag for control, not adding more to the queue when current level contains valid parent, but need to finish whatever left in the queue
3) Use helper method valid parenttheses
"""


""" BFS solution """
from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) == 0: return [s]

        queue = deque() # queue used in BFS
        queue.append(s)
        result = list()
        visited = set()
        found = False # a boolean flag to break loop of adding more neighbors to the queue

        while queue:
            node = queue.popleft()
            if self.isValid(node):
                result.append(node)
                found = True

            if not found:

                for j in xrange(len(node)):
                    # skip when seeing an alphabetical char
                    if node[j] != '(' and node[j] != ')': continue
                    # subs = neighbor of node
                    subs = node[:j] + node[j + 1:]
                    if subs not in visited:
                        queue.append(subs)
                        visited.add(subs)
        return result

    def isValid(self, s):
        counter = 0
        stack = list()
        for c in s:
            if c != '(' and c != ')': continue
            elif c == '(':
                stack.append(')')
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0

""" DFS solution """
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])
        return dfs(s)
