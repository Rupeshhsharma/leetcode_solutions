link- https://leetcode.com/problems/neither-minimum-nor-maximum/description/
code:
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return -1
        nums=sorted(nums)
        for i in range(1,len(nums)-1):
            return nums[i]
            break
