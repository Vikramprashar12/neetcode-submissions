class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs: 
            histogram = [0] * 26 

            for char in string:
                histogram[ord(char)-ord("a")] += 1
            
            res[tuple(histogram)].append(string)
        return res.values()
