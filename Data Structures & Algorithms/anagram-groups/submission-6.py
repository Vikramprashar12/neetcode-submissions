class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []

        for string in strs:
            flag = False
            for index in range(len(results)):
                if sorted(string) == sorted(results[index][0]):
                    results[index].append(string)
                    flag = True
                    break
            if not flag:       
                results.append([string])
            
                
        return results