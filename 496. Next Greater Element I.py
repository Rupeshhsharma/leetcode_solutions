link - https://leetcode.com/problems/next-greater-element-i/description/
code:
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        ans=[0]*len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] >= stack[-1]:
                    stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=-1
            stack.append(nums2[i])
        
        final=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    final.append(ans[j])
                    break
        return final

            


                    
                    

            




        
