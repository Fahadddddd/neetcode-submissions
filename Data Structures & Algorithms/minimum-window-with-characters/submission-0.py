class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        count = {}

        for i in t:
            count[i] = count.get(i, 0) + 1
        
        left = 0
        have = 0
        need = len(t)

        res = ""
        min_len = float('inf')

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1

                if count[s[right]] >= 0:
                    have += 1
            
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]

                if s[left] in count:
                    count[s[left]] += 1

                    if count[s[left]] > 0:
                        have -= 1
                    
                left += 1

        return res



        