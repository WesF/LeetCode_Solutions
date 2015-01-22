"""Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB """
    
class Solution:
    # @return a string
    def convertToTitle(self, num):
        c=''
        _str=''
        mod = 0
        
        while(num>0):
            mod=num%26
            num/=26
            
            if(mod==0):
                num=num-1
                c='Z'
            else:
                c = (chr)(ord('A')+mod-1)
            _str=c+_str
        return _str