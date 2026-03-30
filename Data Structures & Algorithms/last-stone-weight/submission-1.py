class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new = [-s for s in stones] 
        heapq.heapify(new)

        while len(new) > 1:
            val = -heapq.heappop(new)
            val1 = -heapq.heappop(new)
            if val == val1:
                continue
            else:
                heapq.heappush(new, -(max(val, val1) - min(val, val1)))
        
        return -new[0] if new else 0
            
            
