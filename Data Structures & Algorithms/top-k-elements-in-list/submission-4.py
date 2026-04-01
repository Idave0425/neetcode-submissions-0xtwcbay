class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num : # appearances
        # "max heap" --> list of key, value pairs; key negated # experiences
        # ret --> for _ in k, pop from max heap and append to return list 



        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]

        for n, c in freq.items():
            bucket[c].append(n)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
            if len(res) == k:
                return res


             


        
        





        
        
