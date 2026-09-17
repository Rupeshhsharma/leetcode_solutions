link-https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array
code:
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        maxi=float('-inf')
        ind=0
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                if nums[i] > maxi and nums[i]<target:
                    maxi=nums[i]
                    ind=i+1
        return (ind)
        
        
