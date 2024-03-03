class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n)
        else:
            return 1 / self.helper(x, -n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                return self.myPow(x * x, n / 2)
            else:
                return x * self.myPow(x * x, (n - 1) / 2)