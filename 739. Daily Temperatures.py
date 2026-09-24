link- https://leetcode.com/problems/daily-temperatures/description/
code:
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp=temperatures
        stack=[]
        ans=[0]*len(temp)
        for i in range(len(temp)-1,-1,-1):
            while  stack and temp[stack[-1]]<=temp[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i

            stack.append(i)
            
        return ans


        
