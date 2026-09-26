link - https://leetcode.com/problems/valid-anagram/description/
code:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            stack.append(i)
        for j in t:
            if j in stack:
                stack.remove(j)
            else:
                return False
        if stack:
            return False
        else:
            return True
            
        
