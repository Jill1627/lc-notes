class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        self.recur_helper(result, [], s)
        return result
    def recur_helper(self, result, path, ss):
        if len(ss) == 0:
            result.append(list(path))
            return
        for i in range(1, len(ss) + 1):
            if self.isPalindrome(ss[:i]):
                path.append(ss[:i])
                self.recur_helper(result, path, ss[i:])
                path.pop()
    def isPalindrome(self, s):
        if len(s) > 0 and s == s[::-1]:
            return True
        return False
        
