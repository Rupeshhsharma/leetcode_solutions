link-https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=array
code:
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return
        
