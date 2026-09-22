link- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Code:
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low,high=0,len(nums)-1
        first=-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
                pass
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        low,high=0,len(nums)-1
        last=-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        return [first,last]
        
