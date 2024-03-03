class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst, m = [], []
        for i in range(numRows):
            for j in range(i + 1):
                am = factorial(i) // (factorial(i - j) * factorial(j))
                m.append(am)
            lst.append(m)
            m = []
        return lst 