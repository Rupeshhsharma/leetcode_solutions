link- https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/?envType=problem-list-v2&envId=array
code:
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        j=1
        maxi=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                j+=1
            else:
                j=1
            maxi=max(maxi,j)
        return maxi


