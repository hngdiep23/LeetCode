class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [[]] 
        
        for i in range(1, len(nums) + 1):
            s = itertools.combinations(nums, i)
            for j in s:
                lst.append(list(j))
        
        return lst