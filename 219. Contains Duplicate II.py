link- https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=hash-table
code:
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash={}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=i
            else:
                if i-hash[nums[i]]<=k:
                    return True
                hash[nums[i]]=i
        return False

            
      
