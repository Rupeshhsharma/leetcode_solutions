link- https://leetcode.com/problems/digit-frequency-score/description/
code:
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sumi=0
        while n>0:
            x=n%10
            sumi=sumi+x
            print(sumi)
            n=n//10
        return (sumi)
        
