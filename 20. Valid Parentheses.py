link-https://leetcode.com/problems/valid-parentheses/description/ 
code:
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={
            '}':'{',
            ')':'(',
            ']':'[',
        }
        for i in s:
            if i not in dict:
                stack.append(i)  
            else:
                if not stack:
                    return False
                top=stack[-1]
                if dict[i]==top:
                    stack.pop()
                if dict[i]!=top:
                    break 
        if not stack:
            return True
        else:
            return False            

