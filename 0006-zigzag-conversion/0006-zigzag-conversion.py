class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        srt = [""] * numRows
        if numRows == 1 or n == 1:
            return s
        row = 0
        for i in range(n):
            srt[row] += s[i]
            if row == numRows - 1:
                step = 1
            elif row == 0:
                step = 0
            
            if step == 1:
                row -= 1
            else:
                row += 1
        return "".join(x for x in srt)