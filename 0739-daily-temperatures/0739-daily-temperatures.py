class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0] * len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                lst[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return lst