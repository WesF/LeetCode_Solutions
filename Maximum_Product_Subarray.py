"""Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6."""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        _min = _max = MAX = A[0]
        
        for i in range(1,len(A)):
            Temp=[A[i],A[i]*_min,A[i]*_max]
            _min, _max = min(Temp), max(Temp)
            MAX = max(_max, MAX)
            print _min,_max,MAX
        
        return MAX