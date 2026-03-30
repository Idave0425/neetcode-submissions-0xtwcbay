class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            return p[0]**2 + p[1]**2

        
        new = []
        heapq.heapify(new)

        for p in points:
            heapq.heappush(new, (-distance(p), p))

            if len(new) > k:
                heapq.heappop(new)

        
        return [p for (_, p) in new]
        