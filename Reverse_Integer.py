"""Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321"""

class Solution:
    # @return an integer
    def reverse(self, x):
        integer=0
        if abs(x)>2147483647:
            return 0
        if x<0:
            x=str(x*-1)
            
            integer= int(x[::-1])*-1
        else:
            x=str(x)
            integer= int(x[::-1])
        if  abs(integer)>2147483647:
            return 0
        return integer