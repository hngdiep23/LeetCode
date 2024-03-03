class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs]
        elif len(strs) == 1:
            return [strs]
        dct = {}
        for i in range(len(strs)):
            sorted_ = "".join(sorted(strs[i]))
            if sorted_ not in dct.keys():
                dct[sorted_] = [strs[i]]
            else:
                dct[sorted_].append(strs[i])
        return dct.values()