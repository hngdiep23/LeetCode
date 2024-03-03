class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        min_len = min(len(first_str), len(last_str))
        
        result = ""
        for i in range(min_len):
            if first_str[i] == last_str[i]:
                result += first_str[i]
            else:
                break
        
        return result

# Sử dụng lớp Solution để tìm tiền tố chung dài nhất
solution = Solution()
strs = ["flower", "flow", "flight", "false"]
print(solution.longestCommonPrefix(strs))