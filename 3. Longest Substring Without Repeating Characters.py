link- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=hash-table&
code:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hash=[]
        sumi=0
        for i in s:
            while i in hash:
                hash.pop(0)
            hash.append(i)
            l=len(hash)
            sumi=max(sumi,l)
        return sumi
        
        
