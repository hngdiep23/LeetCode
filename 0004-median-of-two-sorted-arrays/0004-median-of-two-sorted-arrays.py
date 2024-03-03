class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        if len(X) > len(Y):
            X, Y = Y, X
        l, r = -1, len(X) - 1
        total = len(X) + len(Y)
        half = total // 2
        while l <= r:
            pivotX = (l + r) // 2
            pivotY = half - pivotX - 2
            leftX = X[pivotX] if pivotX >= 0 else float('-inf')
            rightX = X[pivotX + 1] if pivotX + 1 < len(X) else float('inf')
            leftY = Y[pivotY] if pivotY >= 0 else float('-inf')
            rightY = Y[pivotY + 1] if pivotY + 1 < len(Y) else float('inf')

            if leftX <= rightY and leftY <= rightX:
                if total % 2:
                    return min(rightX, rightY)
                else:
                    return (max(leftX, leftY) + min(rightX, rightY)) /2
            if leftX > rightY:
                r = pivotX - 1
            else:
                l = pivotX + 1     