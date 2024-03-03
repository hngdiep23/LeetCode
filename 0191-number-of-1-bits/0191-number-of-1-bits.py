class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        n = n[2:]
        return n.count('1')