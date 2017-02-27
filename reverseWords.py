class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        return " ".join(sList[::-1])



""" below is java solution """
String[] parts = s.trim().split("\\s+");
String out = "";
for (int i = parts.length - 1; i > 0; i--) {
    out += parts[i] + " ";
}
return out + parts[0];
