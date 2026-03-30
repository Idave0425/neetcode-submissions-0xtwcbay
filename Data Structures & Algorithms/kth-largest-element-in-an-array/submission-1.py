class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        new = [-num for num in nums]
        heapq.heapify(new)

        for i in range(k):
            if i == k - 1:
                return -(heapq.heappop(new))
            
            heapq.heappop(new)