class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lst, s = [], ""
        dct = {'2': 'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits is "":
            return lst
        a = len(digits)
        if a == 1:
            return [x for x in dct[digits]]
        else:
            self.recur_approach(digits, dct, lst, s, i = 0)
            return lst
    def recur_approach(self, digits, dct, lst, s, i = 0):
        if i == len(digits):
            lst.append(s)
            return
        for x in dct[digits[i]]:
            self.recur_approach(digits, dct, lst, s + x, i + 1)