class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        acc = 0
        for item in arr2:
            acc ^= item
        ret=0
        for item in arr1:
            ret ^= (item & acc)
        return ret