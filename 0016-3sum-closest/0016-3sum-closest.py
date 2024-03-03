class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_ = 1000000
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                sum_ = nums[i]+nums[l]+nums[r] - target
                
                if abs(sum_) <= abs(min_):
                    min_ = sum_
                    
                if sum_ == 0:
                    return target
                elif sum_ < 0:
                    l += 1
                else:
                    r -= 1
                    
        return min_ + target