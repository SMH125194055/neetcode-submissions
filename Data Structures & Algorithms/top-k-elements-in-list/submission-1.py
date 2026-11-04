class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] =  1 + count.get(i,0)
        # print(count)
        heap = []
        for i in count.keys():
            heapq.heappush(heap,(count[i],i))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        # print(res)
        return res    
                 