link: https://leetcode.com/problems/fibonacci-number/description/
code:
class Solution:
    def fib(self, n: int) -> int:
        lst=[0,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(n):
            x=lst[i]+lst[i+1]
            lst.append(x)
        return lst[n]
        
