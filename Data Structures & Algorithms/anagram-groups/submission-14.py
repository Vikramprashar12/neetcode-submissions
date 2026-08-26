class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:
            freqMap = [0]*26
            for s in st:
                freqMap[ord(s)-ord('a')]+=1
            res[tuple(freqMap)].append(st)
        return res.values()