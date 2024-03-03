class Solution:
    def capitalizeTitle(self, title: str) -> str:
        y = []
        x = title.lower().split()
        for i in x:
            if len(i) > 2:
                blank = i[0].upper() + i[1:]
                y.append(blank)
            else:
                y.append(i)
        return (' '.join(y))