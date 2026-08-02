class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for letter in nums:
            dict1[str(letter)] += 1
        
        dict_f = dict(sorted(dict1.items(), key = lambda x: x[1], reverse=True))

        list1 = list(dict_f.keys())[:k]

        return [int(x) for x in list1]
        