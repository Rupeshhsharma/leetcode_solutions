link-https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array
code:
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums)!=len(set(nums)):
            return True
        else:
            return False
