class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        new = []
        heapq.heapify(new)

        for num in nums:
            heapq.heappush(new, num)
            if len(new) > k:
                heapq.heappop(new)
            
        val = heapq.heappop(new)
        return val
