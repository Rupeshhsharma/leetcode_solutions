link- https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=array
code:
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)<3:
            return nums[len(nums)-1]
        else:
            return nums[-3]


        
