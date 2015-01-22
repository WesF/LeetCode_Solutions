"""Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 """
    
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num =0
        for i, ch in enumerate(s[::-1]):
            if i == 0:
                num+=(ord(ch)-64)
            else:
                num+=((ord(ch)-64)*26**i)
        return num