# LC 273 Integer to English words
"""
Strategy;
use a helper function to handle every three digits within a thousand
Recursion

Steps:
1. Build maps lessThan20, tens, thousands
2. Main method: while num > 0: mod 1000 and let helper handles within 3 digits
3. Helper method: three cases 1) base case == 0, return ; 2) < 20 return; 3) < 100, mod 10 append tens, then recursion; 4) all other cases which is between 100 to 999, recursion 
"""


"""This solution is easier to understand"""
class Solution(object):
    lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                     "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        words = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + " " + self.thousands[i] + " " + words
            i += 1
            num /= 1000
        return words.strip()

    def helper(self, num):
        if num == 0: return ""
        if num < 20: return self.lessThan20[num]
        if num < 100: return self.tens[num / 10] + " " + self.helper(num % 10)
        else: return self.helper(num / 100) + " Hundred " + self.helper(num % 100)



def numberToWords(self, num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n/10-2]] + words(n%10)
        if n < 1000:
            return [to19[n/100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n/1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'
