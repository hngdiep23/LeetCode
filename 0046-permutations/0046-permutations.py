class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        lst = []
        
        for j in range(len(nums)):
            k = nums[j]
            p = nums[:j] + nums[j+1:]
            for i in self.permute(p):
                lst.append([k] + i)
                
        return lst