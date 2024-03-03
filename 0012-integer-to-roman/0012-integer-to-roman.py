class Solution:
    def intToRoman(self, num: int) -> str:
        srt = ""
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        j = len(values) - 1
        while num:
            quo = num // values[j]
            num %= values[j]
            while quo:
                srt += symbols[j]
                quo -= 1
            j -= 1
        return srt