class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}

        for num in nums:
            if num not in dictt:
                dictt[num] = 1
            else:
                return True
                
        return False 
                
        
         