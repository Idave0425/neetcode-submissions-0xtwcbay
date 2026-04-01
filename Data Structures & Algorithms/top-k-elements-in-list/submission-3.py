class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num : # appearances
        # "max heap" --> list of key, value pairs; key negated # experiences
        # ret --> for _ in k, pop from max heap and append to return list 

        freq = {}
        minHeap = []
        heapq.heapify(minHeap)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        

        for c, v in freq.items():
            heapq.heappush(minHeap, (v, c))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        

        return [c for (_, c) in minHeap]

             


        
        





        
        
