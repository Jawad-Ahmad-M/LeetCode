class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list1 = []

        for x in strs:
            list1.append(str(sorted(x)))
        
        set1 = set(list1)
        final = []
        results = []

        for word in set1:
            for y in range(len(list1)):
                if word == list1[y]: 
                    results.append(strs[y])
            final.append(results)
            results = []
         
        return final