class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freqMap = [0]*26
            for c in s:
                freqMap[ord(c)-ord('a')] += 1
            res[tuple(freqMap)].append(s)
        return list(res.values())

        