class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort()
        cur, streak = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                streak = max(streak, cur)
                cur = 1
        streak = max(streak, cur)
        return streak