class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in s[left:right]: # s[0] in s[0:0] 'z' in "" s[left:right] does not include right.
                left += 1 
            longest = max(longest, right - left + 1)
        return longest  
        