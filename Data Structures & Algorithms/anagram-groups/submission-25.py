class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            freqMap = [0]*26

            for s in string:
                freqMap[ord(s)-ord("a")] += 1

            res[tuple(freqMap)].append(string)
            print(res)
        return res.values()

