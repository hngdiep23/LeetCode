class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {"I": 1, 
                 "V": 5,
                 "X": 10, 
                 "L": 50, 
                 "C": 100, 
                 "D": 500, 
                 "M": 1000}
        
        ans = 0
        length = len(s)

        for i in range(length):
            if i < length - 1 and chars[s[i]] < chars[s[i+1]]:
                ans -= chars[s[i]]
            else:
                ans += chars[s[i]]

        return ans

# Sử dụng lớp Solution để chuyển đổi số La Mã thành số nguyên
solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s))